import nltk

from prompt_optimizer.poptim.base import PromptOptim


class NameReplaceOptim(PromptOptim):
    """
    NameReplaceOptim is a prompt optimization technique based on replacing names in the prompt.
    Some names have lower token count (1) than others. Higher token count names can be replaced by
    such names to reduce token complexity. `self.opti_names` contains the pre-made list of such names
    for `tiktokenizer`. The list will need to be modified for other tokenizers.

    It inherits from the PromptOptim base class.

    Example:
        >>> from prompt_optimizer.poptim import NameReplaceOptim
        >>> p_optimizer = NameReplaceOptim()
        >>> res = p_optimizer("example prompt...")
        >>> optimized_prompt = res.content
    """

    def __init__(self, verbose: bool = False, metrics: list = []):
        """
        Initializes the NameReplaceOptim.

        Args:
            verbose (bool, optional): Flag indicating whether to enable verbose output. Defaults to False.
            metrics (list, optional): A list of metric names to evaluate during optimization. Defaults to an empty list.
        """
        super().__init__(verbose, metrics)
        self.opti_names = self.get_opti_names()

    def download(self):
        """
        Downloads the required NLTK resources.
        """
        nltk.download("punkt")
        nltk.download("averaged_perceptron_tagger")
        nltk.download("maxent_ne_chunker")
        nltk.download("words")

    def process(self, text: str) -> nltk.Tree:
        """
        Processes the text using NLTK to identify named entities.

        Args:
            text (str): The text to process.

        Returns:
            nltk.Tree: The parsed sentence tree containing named entities.
        """
        tokens = nltk.tokenize.word_tokenize(text)
        pos = nltk.pos_tag(tokens)
        sentence_tree = nltk.ne_chunk(pos, binary=False)
        return sentence_tree

    def get_opti_names(self) -> list:
        """
        Retrieves the list of optimized names.

        Returns:
            list: The list of optimized names.
        """
        opti_names = """Rene
            Asa
            Zion
            Avery
            Gray
            Morgan
            Story
            Arden
            Kit
            Lux
            Sol
            Avery
            Pat
            Sky
            Arden
            Clair
            Storm
            Ellery
            Arin
            Sol
            Alpha
            Arie
            Rio
            Isa
            Aris
            Ara
            Adel
            Tam
            Lin
            Aly
            Bao
            Tru
            True
            Toy
            Adi
            Cache
            Chi
            Han
            Amil
            Amel
            Eri
            Truth
            Hoa
            Indy
            Vertis
            Chai
            Ottie
            Ary
            Aki
            Rei
            Bay
            Ova
            Shell
            Rael
            Gal
            Sher
            Elim
            Dae
            Zell
            Wen
            Audi"""
        opti_names = [name.strip() for name in opti_names.split()]
        return opti_names

    def gen_name_map(self, text: str) -> dict:
        """
        Generates a mapping of names in the prompt to optimized names.

        Args:
            text (str): The prompt text.

        Returns:
            dict: The mapping of names to optimized names.
        """
        name_list = []
        try:
            sentence_tree = self.process(text)
        except Exception:
            self.download()
            sentence_tree = self.process(text)

        for subtree in sentence_tree.subtrees(filter=lambda t: t.label() == "PERSON"):
            person = []
            name = ""

            for leaf in subtree.leaves():
                person.append(leaf[0])

            if len(person) > 1:
                for part in person:
                    name += part + " "

                name = name.strip()

                if name not in name_list:
                    name_list.append(name)

        mapping = dict(zip(name_list[: len(self.opti_names)], self.opti_names))
        return mapping

    def opti_name_replace(self, text: str, mapping: dict) -> str:
        """
        Replaces names in the text with optimized names based on the mapping.

        Args:
            text (str): The text to perform name replacement.
            mapping (dict): The mapping of names to optimized names.

        Returns:
            str: The text with replaced names.
        """
        for old_name in mapping:
            new_name = mapping[old_name]
            text = text.replace(old_name, new_name)
        return text

    def optimize(self, prompt: str) -> str:
        """
        Runs the prompt optimization technique on the prompt.

        Args:
            prompt (str): The prompt text.

        Returns:
            str: The optimized prompt text.
        """
        mapping = self.gen_name_map(prompt)
        opti_prompt = self.opti_name_replace(prompt, mapping)
        return opti_prompt
