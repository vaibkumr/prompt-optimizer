from tests.unit_tests import utils
from prompt_optimizer.poptim import (
    AutocorrectOptim,
    LemmatizerOptim,
    PunctuationOptim,
    Sequential,
)


def test_sequential():
    prompt = utils.load_prompt("prompt1.txt")

    p_optimizer = Sequential(
        LemmatizerOptim(verbose=True),
        PunctuationOptim(verbose=True),
        AutocorrectOptim(verbose=True),
    )
    optimized_prompt = p_optimizer(prompt)
    assert len(optimized_prompt) > 0, "Failed!"
