# PromptOptimizer
Minimize LLM token complexity to save API costs and computations.

[![lint](https://github.com/TimeTraveller-San/prompt-optimizer/actions/workflows/lint.yml/badge.svg)](https://github.com/TimeTraveller-San/prompt-optimizer/actions/workflows/lint.yml) [![test](https://github.com/TimeTraveller-San/prompt-optimizer/actions/workflows/test.yml/badge.svg)](https://github.com/TimeTraveller-San/prompt-optimizer/actions/workflows/test.yml) [![linkcheck](https://github.com/TimeTraveller-San/prompt-optimizer/actions/workflows/linkcheck.yml/badge.svg)](https://github.com/TimeTraveller-San/prompt-optimizer/actions/workflows/linkcheck.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


# Features
- **Plug and Play Optimizers:** Minimize token complexity using optimization methods without any access to weights, logits or decoding algorithm. Directly applicable to virtually all NLU systems.
- **Protected Tags:** Special protected tags to mark important sections of prompt that should not be removed/modified.
- **Multiple Input Format Support:** Optmization of string, batches of strings and JSON prompt data with an option to skip system prompts.
- **Sequential Optimization:** Chain different optimizers together sequentially.
- **Optimization Metrics:** Number of tokens reduced and semantic similarity before and after optimization.

# Why?
- **Minimize Token Complexity:** Token Complexity is the amount of prompt tokens required to achieve a given task. Reducing token complexity corresponds to linearly reducing API costs and quadratically reducing computational complexity of usual transformer models.
- **Save Money:** For large businesses, saving 10% on token count can lead to saving 100k USD per 1M USD.
- **Extend Limitations:** Some models have small context lengths, prompt optimizers can help them process larger than context documents.

# Why does it work?
1. LLMs are powerful, they can infill missing information.
2. Natural language is bulky, large words and phrases can be replaced by smaller ones.

| Prompt | # Tokens | Correct Response? |  
| ------------------------------------------------------- | ---------- | ------------------- |  
| Who is the president of the United States of America? | 11 | ✅ |  
| Who president US | 3  (-72%) | ✅ |


# Disclaimer
There is a compression vs performance tradeoff -- the increase in compression comes at the cost of loss in model performance. The tradeoff can be greatly mitigated by chosing the right optimize for a given task. There is no single optimizer for all cases. There is no Adam here.

# Installation
```pip install prompt-optimizer```

# Getting started

```python

from prompt_optimizer.poptim import EntropyOptim

prompt = """The Belle Tout Lighthouse is a decommissioned lighthouse and British landmark located at Beachy Head, East Sussex, close to the town of Eastbourne."""
p_optimizer = EntropyOptim(verbose=True, p=0.1)
optimized_prompt = p_optimizer(prompt)
print(optimized_prompt)

```
# Evaluations
Following are the results for [logiqa](https://github.com/openai/evals/blob/main/evals/registry/evals/logiqa.yaml) OpenAI evals task. It is only performed for first 100 samples. Please note the results over this task are not true for all other tasks, more thorough testing and domain knowledge is needed to choose the optimal optimizer.

| Name | % Tokens Reduced | LogiQA Accuracy | USD Saved Per $100 |
| --- | --- | --- | --- |
| Default | 0.0 | 0.32 | 0.0 |
| Entropy_Optim_p_0.05 | 0.06 | 0.3 | 6.35 |
| Entropy_Optim_p_0.1 | 0.11 | 0.28 | 11.19 |
| Entropy_Optim_p_0.25 | 0.26 | 0.22 | 26.47 |
| Entropy_Optim_p_0.5 | 0.5 | 0.08 | 49.65 |
| SynonymReplace_Optim_p_1.0 | 0.01 | 0.33 | 1.06 |
| Lemmatizer_Optim | 0.01 | 0.33 | 1.01 |
| Stemmer_Optim | -0.06 | 0.09 | -5.91 |
| NameReplace_Optim | 0.01 | 0.34 | 1.13 |
| Punctuation_Optim | 0.13 | 0.35 | 12.81 |
| Autocorrect_Optim | 0.01 | 0.3 | 1.14 |
| Pulp_Optim_p_0.05 | 0.05 | 0.31 | 5.49 |
| Pulp_Optim_p_0.1 | 0.1 | 0.25 | 9.52 |
