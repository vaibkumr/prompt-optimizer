from abc import ABC, abstractmethod

from .logger import logger


class PromptOptimize(ABC):
    """
    PromptOptimize is an abstract base class for prompt optimization techniques.

    It defines the common structure and interface for prompt optimization.

    This class inherits from ABC (Abstract Base Class).
    """

    def __init__(self, verbose: bool = False, metrics: list = []):
        """
        Initializes the PromptOptimize.

        Args:
            verbose (bool, optional): Flag indicating whether to enable verbose output. Defaults to False.
            metrics (list, optional): A list of metric names to evaluate during optimization. Defaults to an empty list.
        """
        self.metrics = metrics
        self.verbose = verbose

    @abstractmethod
    def run(self, prompt: str) -> str:
        """
        Abstract method to run the prompt optimization technique.

        This method must be implemented by subclasses.

        Args:
            prompt (str): The prompt text.

        Returns:
            str: The optimized prompt text.
        """
        pass

    def run_json(self, json_data: dict) -> dict:
        """
        Applies prompt optimization to a JSON data object.

        Args:
            json_data (dict): The JSON data object.

        Returns:
            dict: The JSON data object with the content field replaced by the optimized prompt text.
        """
        json_data["content"] = self.run(json_data["content"])
        return json_data

    def batch_run(self, data: list, skip_system: bool = False, json: bool = True) -> list:
        """
        Applies prompt optimization to a batch of data.

        Args:
            data (list): A list of prompts or JSON data objects.
            skip_system (bool, optional): Flag indicating whether to skip system role data objects. Defaults to False.
            json (bool, optional): Flag indicating whether the input data is in JSON format. Defaults to True.

        Returns:
            list: A list of optimized prompts or JSON data objects.
        """
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

    def __call__(self, prompt: str) -> str:
        """
        Calls the run method to perform prompt optimization.

        Args:
            prompt (str): The prompt text.

        Returns:
            str: The optimized prompt text.
        """
        opti_prompt = self.run(prompt)
        if self.verbose:
            for metric in self.metrics:
                out = metric(prompt, opti_prompt)
                for key in out:
                    logger.info(f"Metric {key}: {out[key]:.3f}")
                    logger.info(f"Prompt Before: {prompt}")
                    logger.info(f"Prompt After: {opti_prompt}")
        return opti_prompt
