import nltk

from prompt_optimizer.poptim.base import PromptOptim


class StopWordOptim(PromptOptim):
    """
    StopWordOptim is a prompt optimization technique that removes stop words from the prompt.

    Stop words are commonly used words (e.g., "the", "is", "in") that are often considered insignificant in natural language processing tasks.

    Example:
        >>> from prompt_optimizer.poptim import StopWordOptim
        >>> p_optimizer = StopWordOptim()
        >>> res = p_optimizer("example prompt...")
        >>> optimized_prompt = res.content

    """

    def __init__(self, verbose: bool = False, metrics: list = []):
        """
        Initializes the StopWordOptim object with the specified parameters.

        Args:
            verbose (bool, optional): If True, print verbose information during optimization. Defaults to False.
            metrics (list, optional): List of metrics to evaluate the optimization. Defaults to [].
        """
        super().__init__(verbose, metrics)
        try:
            self.stop_words = set(nltk.corpus.stopwords.words("english"))
        except Exception:
            nltk.download("stopwords")
            self.stop_words = set(nltk.corpus.stopwords.words("english"))

    def optimize(self, prompt: str) -> str:
        """
        Removes stop words from the prompt.

        Args:
            prompt (str): The input prompt.

        Returns:
            str: The optimized prompt after removing stop words.
        """
        words = prompt.split()
        filtered_words = [word for word in words if word.lower() not in self.stop_words]
        opti_prompt = " ".join(filtered_words)
        return opti_prompt
