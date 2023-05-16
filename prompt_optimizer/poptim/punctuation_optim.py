import string

from prompt_optimizer.poptim.base import PromptOptimize


class PunctuationOptim(PromptOptimize):
    """
    PunctuationOptim is a prompt optimization technique that removes punctuation marks from the prompt.

    It inherits from the PromptOptimize base class.
    """

    def __init__(self, verbose: bool = False, metrics: list = []):
        """
        Initializes the PunctuationOptim.

        Args:
            verbose (bool, optional): Flag indicating whether to enable verbose output. Defaults to False.
            metrics (list, optional): A list of metric names to evaluate during optimization. Defaults to an empty list.
        """
        super().__init__(verbose, metrics)

    def run(self, prompt: str) -> str:
        """
        Runs the prompt optimization technique on the prompt.

        Args:
            prompt (str): The prompt text.

        Returns:
            str: The optimized prompt text with punctuation marks removed.
        """
        opti_prompt = prompt.translate(str.maketrans("", "", string.punctuation))
        return opti_prompt
