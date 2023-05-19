import string

from prompt_optimizer.poptim.base import PromptOptim


class PunctuationOptim(PromptOptim):
    """
    PunctuationOptim is a prompt optimization technique that removes punctuation marks from the prompt.
    LLMs can infer punctuations themselves in most cases, remove them.

    It inherits from the PromptOptim base class.

    Example:
        >>> from prompt_optimizer.poptim import PunctuationOptim
        >>> p_optimizer = PunctuationOptim()
        >>> res = p_optimizer("example prompt...")
        >>> optimized_prompt = res.content
    """

    def __init__(self, verbose: bool = False, metrics: list = [], **kwargs):
        """
        Initializes the PunctuationOptim.

        Args:
            verbose (bool, optional): Flag indicating whether to enable verbose output. Defaults to False.
            metrics (list, optional): A list of metric names to evaluate during optimization. Defaults to an empty list.
        """
        super().__init__(verbose, metrics, **kwargs)

    def optimize(self, prompt: str) -> str:
        """
        Runs the prompt optimization technique on the prompt.

        Args:
            prompt (str): The prompt text.

        Returns:
            str: The optimized prompt text with punctuation marks removed.
        """
        opti_prompt = prompt.translate(str.maketrans("", "", string.punctuation))
        return opti_prompt
