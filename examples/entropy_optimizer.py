from prompt_optimizer.metric import TokenMetric
from prompt_optimizer.poptim import EntropyOptim
from prompt_optimizer.visualize import StringDiffer


prompt = """The Belle Tout Lighthouse is a decommissioned lighthouse and British landmark located at Beachy Head, East Sussex, close to the town of Eastbourne."""
p_optimizer = EntropyOptim(verbose=False, p=0.1, metrics=[TokenMetric()])
optimized_prompt = p_optimizer(prompt).content
sd = StringDiffer()
sd(prompt, optimized_prompt)

