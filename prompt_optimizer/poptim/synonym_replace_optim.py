import string
import random
import tiktoken
from nltk.corpus import wordnet

from prompt_optimizer.poptim.base import PromptOptimize


class SynonymReplaceOptim(PromptOptimize):
    def __init__(self, verbose=False, metrics=[], p=0.5):
        super().__init__(verbose, metrics)
        self.p = p
        self.tokenizer = tiktoken.get_encoding("cl100k_base")

    def get_word_pos(self, word):
        pos = wordnet.synset(word + ".n.01").pos()
        if pos.startswith("n"):
            return "n"
        elif pos.startswith("v"):
            return "v"
        elif pos.startswith("a"):
            return "a"
        elif pos.startswith("r"):
            return "r"
        else:
            return None

    def syn_replace(self, word):
        best_replacement = word
        # try:
        #     pos = self.get_word_pos(word)
        # except:
        #     return best_replacement

        # if pos:
        best_l = len(self.tokenizer.encode(word))
        if best_l > 1:
            for syn in wordnet.synsets(word):
                for lemma in syn.lemmas():
                    synonym_word = lemma.name()
                    l_new = len(self.tokenizer.encode(synonym_word))
                    if l_new < best_l:
                        best_replacement = synonym_word
        return best_replacement

    def run(self, prompt):
        """higher p = more replacements"""
        words = prompt.split()
        opti_words = []
        for word in words:
            new_word = self.syn_replace(word)
            if new_word != word and random.uniform(0, 1) <= self.p:
                opti_words.append(new_word)
            else:
                opti_words.append(word)

        return " ".join(opti_words)
