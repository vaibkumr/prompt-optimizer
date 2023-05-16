from tests.unit_tests import utils
from prompt_optimizer.metric import TokenMetric
from prompt_optimizer.poptim import EntropyOptim

def test_entropy_optim():
    prompt = utils.load_prompt("prompt1.txt")
    p_optimizer = EntropyOptim(verbose=True, p=0.1, metrics=[TokenMetric()])
    optimized_prompt = p_optimizer(prompt)
    assert len(optimized_prompt) > 0, "Failed!"
