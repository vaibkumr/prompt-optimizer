import os
from prompt_optimizer.metric import BERTScoreMetric, TokenMetric
from prompt_optimizer.poptim import SynonymReplaceOptim


def load_prompt(prompt_f):
    file_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "data", prompt_f)
    )
    with open(file_path, "r") as f:
        data = f.read()
    return data


prompt = load_prompt("prompt1.txt")
p_optimizer = SynonymReplaceOptim(verbose=True, p=1.0, metrics=[TokenMetric()])
optimized_prompt = p_optimizer(prompt)
print(optimized_prompt)
