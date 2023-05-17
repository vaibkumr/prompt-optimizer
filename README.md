# PromptOptimizer
Minimize LLM tokens to save API costs and increase limits.

[![lint](https://github.com/TimeTraveller-San/prompt-optimizer/actions/workflows/lint.yml/badge.svg)](https://github.com/TimeTraveller-San/prompt-optimizer/actions/workflows/lint.yml) [![test](https://github.com/TimeTraveller-San/prompt-optimizer/actions/workflows/test.yml/badge.svg)](https://github.com/TimeTraveller-San/prompt-optimizer/actions/workflows/test.yml) [![linkcheck](https://github.com/TimeTraveller-San/prompt-optimizer/actions/workflows/linkcheck.yml/badge.svg)](https://github.com/TimeTraveller-San/prompt-optimizer/actions/workflows/linkcheck.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Why?
- Large Language Models read text after breaking them into tokens. 
- The pricing of APIs is linearly propotional to number of tokens.
- The computational complexity of transformer models is usually quadratic to the number of tokens. 
- For large businesses, saving 10% on token count can lead to saving 100k USD per 1M USD.

# Disclaimer
There is a compression vs performance tradeoff -- the increase in compression comes at a loss in model performance. The tradeoff can be greatly mitigated by chosing the right optimize for a given task. There is no single optimizer for all cases. There is no Adam.

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
