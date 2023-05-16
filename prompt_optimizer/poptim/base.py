from abc import ABC, abstractmethod

from .logger import logger


class PromptOptimize(ABC):
    def __init__(self, verbose=False, metrics=[]):
        self.metrics = metrics
        self.verbose = verbose

    @abstractmethod
    def run(self, prompt):
        pass

    def run_json(self, json_data):
        json_data["content"] = self.run(json_data["content"])
        return json_data

    def batch_run(self, data, skip_system=False, json=True):
        optimized_data = []
        for d in data:
            if json:
                if skip_system and d["role"] == "system":
                    optimized_data.append(d)
                else:
                    optimized_data.append(self.run_json(d))
            else:
                optimized_data.append(self.run(d))
        return optimized_data

    def __call__(self, prompt):
        opti_prompt = self.run(prompt)
        if self.verbose:
            for metric in self.metrics:
                out = metric(prompt, opti_prompt)
                for key in out:
                    logger.info(f"Metric {key}: {out[key]:.3f}")
                    logger.info(f"Prompt Before: {prompt}")
                    logger.info(f"Prompt After: {opti_prompt}")
        return opti_prompt
