from tests.unit_tests import utils
from prompt_optimizer.poptim import PunctuationOptim


def test_punctuation_optim():
    prompt = "Yharnam is a fictional city that is the primary setting of Bloodborne <pt>,</pt> a 2015 video game developed by FromSoftware."
    p_optimizer = PunctuationOptim(protect_tag="pt", verbose=True)
    optimized_prompt = p_optimizer(prompt)
    print(prompt)
    print(optimized_prompt)
    assert "," in optimized_prompt.content, "protect tags not working"
