from tests.unit_tests import utils
from prompt_optimizer.metric import TokenMetric
from prompt_optimizer.poptim import NameReplaceOptim



def test_name_replace_optim():
    prompt = utils.load_prompt("prompt2.txt")
    p_optimizer = NameReplaceOptim(verbose=True, metrics=[TokenMetric()])
    optimized_prompt = p_optimizer(prompt)
    assert len(optimized_prompt) > 0, "Failed!"
