from prompt_optimizer.poptim.base import PromptOptimize
from nltk.stem import PorterStemmer


class StemmerOptim(PromptOptimize):
    """This doesn't really reduce #tokens"""
    def __init__(self, verbose=False, metrics=[]):
        super().__init__(verbose, metrics)
        self.stemmer = PorterStemmer()

    
    def run(self, prompt):
        words = prompt.split()
        stemmed_words = [self.stemmer.stem(word) for word in words]
        opti_prompt = ' '.join(stemmed_words)
        return opti_prompt