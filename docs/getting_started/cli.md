# PromptOptimizer CLI
PromptOptimizer provides a command line interface `prompt_optimizer.cli.main:main` to run prompt optimizations and metrics.

- Type `prompt-optimizer --help` on the command line:

```

usage: prompt-optimizer [-h] [--json JSON] [--skip_system SKIP_SYSTEM]
                        [--optimizer_args [OPTIMIZER_ARGS ...]] [--metrics [METRICS ...]]
                        [--log_file LOG_FILE]
                        prompt_data_or_path optimizer_name

Prompt Optimizer CLI

positional arguments:
  prompt_data_or_path   Either the prompt data (string or json string) or path to a file containing new
                        line separated prompt data.
  optimizer_name        Name of the optimizer.

options:
  -h, --help            show this help message and exit
  --json JSON           Prompt format JSON or not.
  --skip_system SKIP_SYSTEM
                        Skip system prompts or not. Only valid if `json` is True.
  --optimizer_args [OPTIMIZER_ARGS ...]
                        Additional arguments for the optimizer.
  --metrics [METRICS ...]
                        List of metrics to compute.
  --log_file LOG_FILE   Output file to append results to. Prints on `stdout` if `None`.
```

Some [Examples](https://github.com/vaibkumr/prompt-optimizer/tree/master/examples/cli) are given to get started with CLI!