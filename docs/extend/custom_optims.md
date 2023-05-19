# Creating Custom PromptOptimizers
All prompt optimizers must extend the `from prompt_optimizer.poptim.PromptOptim` class. 

A custom `MyCustomOptim` optimizer will look as follows:

```python
from prompt_optimizer.poptim.base import PromptOptim

class MyCustomOptim(PromptOptim):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def optimize(self, prompt: str) -> str:
        opti_prompt = prompt
        return opti_prompt
```

to create an optimizer, we just need to implement the `optimize` function that takes input a string and outputs another string that is optimized. 

If you implement some optimizers, please consider contributing them to this project.