from nltk.stem import PorterStemmer

from prompt_optimizer.poptim.base import PromptOptim


class StemmerOptim(PromptOptim):
    """
    StemmerOptim is a prompt optimization technique that applies stemming to the prompt.

    Stemming reduces words to their base or root form, removing suffixes and prefixes.

    Example:
        >>> from prompt_optimizer.poptim import StemmerOptim
        >>> p_optimizer = StemmerOptim()
        >>> res = p_optimizer("example prompt...")
        >>> optimized_prompt = res.content

    """

    def __init__(self, verbose: bool = False, metrics: list = []):
        """
        Initializes the StemmerOptim object with the specified parameters.

        Args:
            verbose (bool, optional): If True, print verbose information during optimization. Defaults to False.
            metrics (list, optional): List of metrics to evaluate the optimization. Defaults to [].
        """
        super().__init__(verbose, metrics)
        self.stemmer = PorterStemmer()

    def optimize(self, prompt: str) -> str:
        """
        Applies stemming to the prompt.

        Args:
            prompt (str): The input prompt.

        Returns:
            str: The optimized prompt after applying stemming.
        """
        words = prompt.split()
        stemmed_words = [self.stemmer.stem(word) for word in words]
        opti_prompt = " ".join(stemmed_words)
        return opti_prompt
