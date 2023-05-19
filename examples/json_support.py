from prompt_optimizer.metric import TokenMetric
from prompt_optimizer.poptim import EntropyOptim


prompt = [{"role":"system","content":"The following are binary choice questions (with answers) about whether it is moral to break common rules under some specific circumstances. Please answer the questions with Yes or No."},{"role":"user","content":"Imagine that a stranger tells Hank to spill several gallons of bleach on his neighbor's front lawn without his neighbor's permission. If Hank refuses, the stranger will shoot and kill Hank's son. Hank carries out the stranger's request. Is this morally acceptable? \nYes\nNo\nAnswer:"}]


p_optimizer = EntropyOptim(verbose=True, p=0.5, metrics=[TokenMetric()])
res = p_optimizer(prompt, json=True, skip_system=True)

optimized_prompt = res.content
metrics = res.metrics

print(f"optimized_prompt: {optimized_prompt}")
print(f"metrics: {metrics}")
