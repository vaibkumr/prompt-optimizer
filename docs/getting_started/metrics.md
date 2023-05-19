# Metrics
Given a prompt and its corresponding optimized prompt, we can compute several metrics for sanity checks, logging and more. We might need to check the percentage of tokens saved, semantic similarity between optimized and original prompt text (BERTScore), sentiment before and after optimization and much more. All of this can be done by extending the `prompt_optimizer.metric.Metric` class.

# Running Metrics
All metrics extend the `prompt_optimizer.metric.Metric` abstract class. 
To evaluate a metric, pass the list of metric objects in the `metrics` keyword argument of the prompt object as follows:

```python
from prompt_optimizer.metric import TokenMetric
from prompt_optimizer.poptim import StopWordOptim

p_optimizer = StopWordOptim(metrics=[TokenMetric()])
```
After specifying a metric, the prompt result object has an additional key `metrics` that contains the list of dictionaries with key as the metric name string and value as the computed metric value.


```python
prompt = """The Belle Tout Lighthouse is a decommissioned lighthouse and British landmark located at Beachy Head, East Sussex, close to the town of Eastbourne. """
res = p_optimizer(prompt)
for metric in res.metrics:
    for key, value in res.metrics.items():
        print(f"{key}: {value:.3f}")
```

A list of all metrics can be found here.