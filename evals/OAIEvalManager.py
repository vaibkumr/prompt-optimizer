import json
import langchain
import evals
import evals.api
import evals.base
import evals.record
from evals.eval import Eval
from evals.registry import Registry

#---------------------------------------
import argparse
import logging
import shlex
import sys
from typing import Any, Mapping, Optional, Union, cast

import openai

import evals
import evals.api
import evals.base
import evals.record
from evals.eval import Eval
from evals.registry import Registry

logger = logging.getLogger(__name__)

def _purple(str: str) -> str:
    return f"\033[1;35m{str}\033[0m"

class OaiEvalManager:
    def __init__(self):
        self.completion_fn: str = ""
        self.eval: str = ""
        self.extra_eval_params: str = ""
        self.max_samples: Optional[int] = None
        self.cache: bool = True
        self.visible: Optional[bool] = None
        self.seed: int = 20220722
        self.user: str = ""
        self.record_path: Optional[str] = None
        self.log_to_file: Optional[str] = None
        self.registry_path: Optional[str] = None
        self.debug: bool = False
        self.local_run: bool = True
        self.dry_run: bool = False
        self.dry_run_logging: bool = True
        print(evals.__path__)

    def run(self, registry: Optional[Registry] = None) -> str:
        if self.debug:
            logging.getLogger().setLevel(logging.DEBUG)

        visible = self.visible if self.visible is not None else (self.max_samples is None)

        if self.max_samples is not None:
            evals.eval.set_max_samples(self.max_samples)

        registry = registry or Registry()
        if self.registry_path:
            registry.add_registry_paths(self.registry_path)

        eval_spec = registry.get_eval(self.eval)
        assert (
            eval_spec is not None
        ), f"Eval {self.eval} not found. Available: {list(sorted(registry._evals.keys()))}"

        completion_fns = self.completion_fn.split(",")
        completion_fn_instances = [registry.make_completion_fn(url) for url in completion_fns]

        run_config = {
            "completion_fns": completion_fns,
            "eval_spec": eval_spec,
            "seed": self.seed,
            "max_samples": self.max_samples,
            "command": " ".join(map(shlex.quote, sys.argv)),
            "initial_settings": {
                "visible": visible,
            },
        }

        eval_name = eval_spec.key
        if eval_name is None:
            raise Exception("you must provide a eval name")

        run_spec = evals.base.RunSpec(
            completion_fns=completion_fns,
            eval_name=eval_name,
            base_eval=eval_name.split(".")[0],
            split=eval_name.split(".")[1],
            run_config=run_config,
            created_by=self.user,
        )
        if self.record_path is None:
            record_path = f"/tmp/evallogs/{run_spec.run_id}_{self.completion_fn}_{self.eval}.jsonl"
        else:
            record_path = self.record_path

        recorder: evals.record.RecorderBase
        if self.dry_run:
            recorder = evals.record.DummyRecorder(run_spec=run_spec, log=self.dry_run_logging)
        elif self.local_run:
            recorder = evals.record.LocalRecorder(record_path, run_spec=run_spec)
        else:
            recorder = evals.record.Recorder(record_path, run_spec=run_spec)

        api_extra_options: dict[str, Any] = {}
        if not self.cache:
            api_extra_options["cache_level"] = 0

        run_url = f"{run_spec.run_id}"
        logger.info(_purple(f"Run started: {run_url}"))

        def parse_extra_eval_params(
            param_str: Optional[str],
        ) -> Mapping[str, Union[str, int, float]]:
            """Parse a string of the form "key1=value1,key2=value2" into a dict."""
            if not param_str:
                return {}

            def to_number(x: str) -> Union[int, float, str]:
                try:
                    return int(x)
                except:
                    pass
                try:
                    return float(x)
                except:
                    pass
                return x

            str_dict = dict(kv.split("=") for kv in param_str.split(","))
            return {k: to_number(v) for k, v in str_dict.items()}

        extra_eval_params = parse_extra_eval_params(self.extra_eval_params)

        eval_class = registry.get_class(eval_spec)
        eval: Eval = eval_class(
            completion_fns=completion_fn_instances,
            seed=self.seed,
            name=eval_name,
            registry=registry,
            **extra_eval_params,
        )
        result = eval.run(recorder)
        recorder.record_final_report(result)

        if not (self.dry_run or self.local_run):
            logger.info(_purple(f"Run completed: {run_url}"))

        logger.info("Final report:")
        for key, value in result.items():
            logger.info(f"{key}: {value}")
        return run_spec.run_id

    def execute(self) -> None:
        logging.basicConfig(
            format="[%(asctime)s] [%(filename)s:%(lineno)d] %(message)s",
            level=logging.INFO,
            filename=self.log_to_file if self.log_to_file else None,
        )
        logging.getLogger("openai").setLevel(logging.WARN)
        # TODO)) why do we need this?
        if hasattr(openai.error, "set_display_cause"):  # type: ignore
            openai.error.set_display_cause()  # type: ignore
        self.run()
