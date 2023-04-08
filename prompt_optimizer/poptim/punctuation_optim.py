import string
from prompt_optimizer.poptim.base import PromptOptimize


class PunctuationOptim(PromptOptimize):
    """This doesn't really reduce #tokens"""
    def __init__(self, verbose=False, metrics=[]):
        super().__init__(verbose, metrics)

    
    def run(self, prompt):
        opti_prompt = prompt.translate(str.maketrans('', '', string.punctuation))
        return opti_prompt