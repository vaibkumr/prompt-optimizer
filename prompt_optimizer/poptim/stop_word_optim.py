from prompt_optimizer.poptim.base import PromptOptimize
import nltk
from nltk.corpus import stopwords


class StopWordOptim(PromptOptimize):
    def __init__(self, verbose=False, metrics=[]):
        super().__init__(verbose, metrics)
        if not nltk.corpus.stopwords.words('english'):
            nltk.download('stopwords')
        self.stop_words = set(stopwords.words('english'))
    
    def run(self, prompt):
        words = prompt.split()
        filtered_words = [word for word in words if word.lower() not in self.stop_words]
        opti_prompt = ' '.join(filtered_words)
        return opti_prompt