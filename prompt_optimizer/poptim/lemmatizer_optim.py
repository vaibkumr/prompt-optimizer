import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

from prompt_optimizer.poptim.base import PromptOptimize


class LemmatizerOptim(PromptOptimize):
    def __init__(self, verbose=False, metrics=[]):
        super().__init__(verbose, metrics)
        self.lemmatizer = WordNetLemmatizer()

    def get_wordnet_pos(self, word):
        tag = nltk.pos_tag([word])[0][1][0].upper()
        tag_dict = {
            "J": wordnet.ADJ,
            "N": wordnet.NOUN,
            "V": wordnet.VERB,
            "R": wordnet.ADV,
        }
        return tag_dict.get(tag, wordnet.NOUN)

    def run(self, prompt):
        words = prompt.split()
        lemmatized_words = [
            self.lemmatizer.lemmatize(word, self.get_wordnet_pos(word))
            for word in words
        ]
        opti_prompt = " ".join(lemmatized_words)
        return opti_prompt
