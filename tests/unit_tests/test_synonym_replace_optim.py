from tests.unit_tests import utils
from prompt_optimizer.metric import TokenMetric
from prompt_optimizer.poptim import SynonymReplaceOptim


def test_synonym_replace_optim():
    prompt = utils.load_prompt("prompt1.txt")
    p_optimizer = SynonymReplaceOptim(verbose=True, p=1.0, metrics=[TokenMetric()])
    optimized_prompt = p_optimizer(prompt)
    assert len(optimized_prompt) > 0, "Failed!"
