from prompt_optimizer.poptim import PunctuationOptim


prompt = """The Belle <pt>Tout</pt> Lighthouse is a decommissioned lighthouse and British landmark located at Beachy Head, East Sussex, close to the town of Eastbourne."""
p_optimizer = PunctuationOptim(verbose=True, protect_tag="pt")
optimized_prompt = p_optimizer(prompt)
print("optimized_prompt::: ", optimized_prompt)
