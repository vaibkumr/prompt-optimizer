import nltk

from prompt_optimizer.poptim.base import PromptOptimize


class StopWordOptim(PromptOptimize):
    """
    StopWordOptim is a prompt optimization technique that removes stop words from the prompt.

    Stop words are commonly used words (e.g., "the", "is", "in") that are often considered insignificant in natural language processing tasks.

    Usage:
    ```
    stopword_optim = StopWordOptim()
    optimized_prompt = stopword_optim(prompt)
    ```

    Args:
        verbose (bool, optional): If True, print verbose information during optimization. Defaults to False.
        metrics (list, optional): List of metrics to evaluate the optimization. Defaults to [].

    Attributes:
        stop_words (set): A set of stop words in the English language.

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

    def run(self, prompt: str) -> str:
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
