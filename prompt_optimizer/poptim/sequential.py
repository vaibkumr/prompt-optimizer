from typing import Any, List

from prompt_optimizer.poptim.base import PromptOptim

from .utils import DotDict


class Sequential:
    """
    Sequential is a class that represents a sequential composition of prompt optimization techniques.

    It applies a series of optimization techniques in sequence to the prompt.

    Usage:
    ```
    optim1 = SomeOptimizationTechnique()
    optim2 = AnotherOptimizationTechnique()
    seq = Sequential(optim1, optim2)
    optimized_prompt = seq(prompt)
    ```

    Args:
        *optims: Variable-length argument list of prompt optimization techniques.

    Attributes:
        optims (list): A list of prompt optimization techniques.

    """

    def __init__(self, *optims: PromptOptim):
        """
        Initializes the Sequential object with the specified prompt optimization techniques.

        Args:
            *optims: Variable-length argument list of prompt optimization techniques.
        """
        self.optims: List[PromptOptim] = list(optims)

    def __call__(self, x: Any) -> Any:
        """
        Applies the sequential composition of prompt optimization techniques to the prompt.

        Args:
            x (Any): The input prompt.

        Returns:
            Any: The optimized prompt after applying the sequential optimizations.
        """
        d = DotDict()
        d.content = x
        for optim in self.optims:
            d = optim(d.content)
        return d
