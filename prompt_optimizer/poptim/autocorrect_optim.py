from autocorrect import Speller

from prompt_optimizer.poptim.base import PromptOptim


class AutocorrectOptim(PromptOptim):
    """
    AutocorrectOptim is a prompt optimization technique that applies autocorrection to the prompt text.
    Correctly spelled words have less token count than incorrect ones. This is useful in scenarios where
    human client types the text.

    It inherits from the PromptOptim base class.

    Example:
        >>> from prompt_optimizer.poptim import AutocorrectOptim
        >>> p_optimizer = AutocorrectOptim()
        >>> res = p_optimizer("example prompt...")
        >>> optimized_prompt = res.content
    """

    def __init__(self, fast: bool = False, verbose: bool = False, metrics: list = []):
        """
        Initializes the AutocorrectOptim.

        Args:
            fast (bool, optional): Flag indicating whether to use a fast autocorrect implementation. Defaults to False.
            verbose (bool, optional): Flag indicating whether to enable verbose output. Defaults to False.
            metrics (list, optional): A list of metric names to evaluate during optimization. Defaults to an empty list.
        """
        super().__init__(verbose, metrics)
        self.spell = Speller(lang="en", fast=fast)

    def optimize(self, prompt: str) -> str:
        """
        Applies autocorrection to the prompt text.

        Args:
            prompt (str): The prompt text.

        Returns:
            str: The optimized prompt text after applying autocorrection.
        """
        words = prompt.split()
        autocorrected_words = [self.spell(word) for word in words]
        opti_prompt = " ".join(autocorrected_words)
        return opti_prompt
