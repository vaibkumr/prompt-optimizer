from tests.unit_tests import utils
from prompt_optimizer.metric import BERTScoreMetric, TokenMetric
from prompt_optimizer.poptim import AutocorrectOptim


def test_autocorrect_optim():
    prompt = utils.load_prompt("prompt1.txt")
    p_optimizer = AutocorrectOptim(
        verbose=True, metrics=[TokenMetric(), BERTScoreMetric()]
    )
    optimized_prompt = p_optimizer(prompt)
    assert len(optimized_prompt) > 0, "Failed!"
