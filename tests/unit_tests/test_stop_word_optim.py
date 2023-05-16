from tests.unit_tests import utils
from prompt_optimizer.metric import TokenMetric
from prompt_optimizer.poptim import StopWordOptim


def test_stop_word_optim():
    prompt = utils.load_prompt("prompt1.txt")
    p_optimizer = StopWordOptim(verbose=True, metrics=[TokenMetric()])
    optimized_prompt = p_optimizer(prompt)
    assert len(optimized_prompt) > 0, "Failed!"
