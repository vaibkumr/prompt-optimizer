import tiktoken

from prompt_optimizer.metric.base import Metric


class TokenMetric(Metric):
    """Reduction in number of tokens as tokenized by tiktoken.

    Args:
        tokenizer (str): Name for the tiktoken tokenizer 
                         `cl100k_base` by default.

    """

    def __init__(self, tokenizer="cl100k_base"):
        super().__init__()
        self.tokenizer = tiktoken.get_encoding(tokenizer)

    def run(self, prompt_before, prompt_after):
        n_tokens_before = len(self.tokenizer.encode(prompt_before))
        n_tokens_after = len(self.tokenizer.encode(prompt_after))
        opti_ratio = 100 * (n_tokens_before - n_tokens_after) / n_tokens_before
        return {"num_token_opti_ratio": opti_ratio}

    def __call__(self, prompt_before, prompt_after):
        return self.run(prompt_before, prompt_after)
