from abc import ABC, abstractmethod
from collections import defaultdict


class Metric(ABC):
    def __init__(self):
        self.key = None

    @abstractmethod
    def run(self, prompt_before: str, prompt_after: str) -> dict:
        """
        Abstract method to run the metric on the given prompts.

        Args:
            prompt_before (str): The prompt before the modification.
            prompt_after (str): The prompt after the modification.

        Returns:
            dict: The result of the metric computation.
        """
        pass

    def run_json(self, json_data_before: dict, json_data_after: dict) -> dict:
        """
        Runs the metric on the content of JSON data.

        Args:
            json_data_before (dict): JSON data before the modification with "content" key.
            json_data_after (dict): JSON data after the modification with "content" key.

        Returns:
            dict: The result of the metric computation.
        """
        res = self.run(json_data_before["content"], json_data_after["content"])
        return res

    def batch_run(
        self,
        prompts_before: list,
        prompts_after: list,
        skip_system: bool = False,
        json: bool = False,
        langchain: bool = False,
    ) -> float:
        """
        Runs the metric on a batch of prompts.

        Args:
            prompts_before (list): List of prompts before the modification.
            prompts_after (list): List of prompts after the modification.
            skip_system (bool, optional): Whether to skip prompts with "system" role. Defaults to False.
            json (bool, optional): Whether the prompts are JSON data. Defaults to False.
            langchain (bool, optional): Whether the prompts are langchain chat data. Defaults to False.

        Returns:
            float: The average metric value across the batch.
        """
        avg_m = defaultdict(float)
        n = 0
        for pb, pa in zip(prompts_before, prompts_after):
            if json:
                if skip_system and pb["role"] == "system":
                    continue
                else:
                    res = self.run_json(pb, pa)
                    n += 1

            elif langchain:
                if skip_system and pb.role == "system":
                    continue
                else:
                    res = self.run(pb.content, pa.content)
                    n += 1

            else:
                res = self.run(pb, pa)
                n += 1

            for key in res:
                avg_m[key] += res[key]

        for key in avg_m:
            avg_m[key] /= n

        return avg_m

    def __call__(self, prompt_before: str, prompt_after: str) -> dict:
        """
        Callable method to run the metric on the given prompts.

        Args:
            prompt_before (str): The prompt before the modification.
            prompt_after (str): The prompt after the modification.

        Returns:
            dict: The result of the metric computation.
        """
        return self.run(prompt_before, prompt_after)
