# Quickstart Guide

Welcome to PromptOptimizer! This guide will help you quickly get started with using PromptOptimizer in your projects. PromptOptimizer is a Python library that allows you to minimize token complexity in order to save API costs and reduce model computations.

# Installation
### Quick Installation

To quickly install PromptOptimizer, use the following command:
```bash
pip install prompt-optimizer
```

### Install from Source
If you prefer to install PromptOptimizer from source, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/vaibkumr/prompt-optimizer.git
```
2. Navigate to the cloned repository:
```bash
cd prompt-optimizer
```
3. Install PromptOptimizer using pip:
```bash
pip install -e .
```

# Prompt Optimizers
A prompt optimizer is a callable class that outputs optimized prompt data along with metrics (if requested) for given input prompt data. 

> Note: Optimizers output a result object with keys `content` to store optimized prompts and `metrics` to store the requested metrics computations results.

To optimize a prompt we follow three steps:
1. Import the optimizer from the range of available [../optimizers/index.html](optimizers). For now, we use the `EntropyOptim`.

```python
from prompt_optimizer.poptim import EntropyOptim
```
2. Initialize the optimizer object. Each optimizer has its own argument which can be tuned to achieve a balance between the cost and performance tradeoff. 

```python
p_optimizer = EntropyOptim(p=0.1)
```

3. Run the optimizer over a given prompt string and fetch the results
```python
prompt = "In Nightmare of Mensis progress through until you reach the boss room."
result = p_optimizer(prompt)
optimized_prompt = result.content
```

And we're done! We just optimized our first prompt, saved some money and if we're smart, we had no loss in model performance.

# Input Formats
Prompt optimizers support three different formats:
1. **String:** A basic python string. At the core, all optimizers work on python strings.

```python
from prompt_optimizer.poptim import EntropyOptim
p_optimizer = EntropyOptim(p=0.1)
prompt = "In Nightmare of Mensis progress through until you reach the boss room."
result = p_optimizer(prompt)
optimized_prompt = result.content
```

2. **JSON Object:** APIs often accept instructions in form of sytem and human messages. JSON objects of the following format can be passed to the optimizers using the `json` boolean flag:
```json
[
    {
        "role":"system",
        "content":"System instructions..."
    },
    {
        "role":"user",
        "content":"User prompt..."
    }
]
```
often times, it is important to skip system instructions. It can be done using the `skip_system` flag as follows:

```python
from prompt_optimizer.poptim import EntropyOptim
p_optimizer = EntropyOptim(p=0.1)
prompt = [
    {
        "role":"system",
        "content":"System instructions..."
    },
    {
        "role":"user",
        "content":"User prompt..."
    }
]
optimized_prompt = p_optimizer(prompt, json=True, skip_system=True)
```

3. **Langchain Object:** Langchain agents accept prompts as a list of `SystemMessage` and `HumanMessage`. Prompt optimizers can directly be applied to these objects by using the `langchain` boolean flag. Again, `skip_system` flag can be used to skip optimizing system prompts as follows:

```python
from prompt_optimizer.poptim import EntropyOptim
from langchain.schema import (
    HumanMessage,
    SystemMessage
)

p_optimizer = EntropyOptim(p=0.1)
prompt = [
    SystemMessage(content="You are a helpful assistant that translates English to French."),
    HumanMessage(content="I love programming.")
]
optimized_prompt = p_optimizer(prompt, langchain=True, skip_system=True)
```
