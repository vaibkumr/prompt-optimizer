from prompt_optimizer.metric import BERTScoreMetric
from prompt_optimizer.poptim import StopWordOptim


prompt = """The Belle Tout Lighthouse is a decommissioned lighthouse and British landmark located at Beachy Head, East Sussex, close to the town of Eastbourne. The cliffs near Beachy Head saw numerous shipwrecks in the 17th and early 18th centuries and a petition to erect a lighthouse started around 1691. Despite this, the lighthouse was not built until 1828, initially as a temporary wooden structure, and then as a permanent granite lighthouse which was designed by Thomas Stevenson and became operational in 1834. The light was provided by a three-sided rotating array of oil lamps with ten lamps on each side, each lamp mounted within a parabolic reflector. The Belle Tout lighthouse was decommissioned in 1902, when the replacement Beachy Head Lighthouse was built at the bottom of the cliffs. In 1999, the Grade II listed building was moved in one piece to prevent it from succumbing to coastal erosion, and since 2010 it has operated as a bed and breakfast."""
p_optimizer = StopWordOptim(metrics=[BERTScoreMetric()])

res = p_optimizer(prompt)

print(f"Optmized Prompt: {res.content}")
for key, value in res.metrics[0].items():
    print(f"{key}: {value:.3f}")
