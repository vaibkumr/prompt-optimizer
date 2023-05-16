import nltk
from prompt_optimizer.poptim.base import PromptOptimize


class StopWordOptim(PromptOptimize):
    def __init__(self, verbose=False, metrics=[]):
        super().__init__(verbose, metrics)

        try:
            self.stop_words = set(nltk.corpus.stopwords.words("english"))
        except Exception:
            nltk.download("stopwords")
            self.stop_words = set(nltk.corpus.stopwords.words("english"))

    def run(self, prompt):
        words = prompt.split()
        filtered_words = [word for word in words if word.lower() not in self.stop_words]
        opti_prompt = " ".join(filtered_words)
        return opti_prompt
