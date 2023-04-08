from autocorrect import Speller

from prompt_optimizer.poptim.base import PromptOptimize


class AutocorrectOptim(PromptOptimize):
    def __init__(self, fast=False, verbose=False, metrics=[]):
        super().__init__(verbose, metrics)
        self.spell = Speller(lang="en", fast=fast)

    def run(self, prompt):
        words = prompt.split()
        autocorrected_words = [self.spell(word) for word in words]
        opti_prompt = " ".join(autocorrected_words)
        return opti_prompt
