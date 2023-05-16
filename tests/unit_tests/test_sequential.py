from tests.unit_tests import utils
from prompt_optimizer.metric import TokenMetric
from prompt_optimizer.poptim import (
    AutocorrectOptim,
    LemmatizerOptim,
    PunctuationOptim,
    Sequential,
)


def test_sequential():
    prompt = utils.load_prompt("prompt1.txt")

    p_optimizer = Sequential(
        LemmatizerOptim(verbose=True, metrics=[TokenMetric()]),
        PunctuationOptim(verbose=True, metrics=[TokenMetric()]),
        AutocorrectOptim(verbose=True, metrics=[TokenMetric()]),
    )
    optimized_prompt = p_optimizer(prompt)
    assert len(optimized_prompt) > 0, "Failed!"
