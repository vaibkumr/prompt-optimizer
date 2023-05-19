# Creating Custom Metrics
All metrics are computed between the original and optimized metric. They must extend the `prompt_optimizer.metric.Metric` class. 


A custom `MyCustomMetric` optimizer will look as follows:

```python

from prompt_optimizer.metric.base import Metric

class MyCustomMetric(Metric):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self, prompt_before: str, prompt_after: str) -> dict:
        return {'metric_name': 0.0}
```

to create a custom metric, just implement the `run` function that takes input two strings: `prompt_before` that is the orignial prompt and `prompt_after` that is the prompt after optimizations. The function must return a dictionary with key(s) and value(s) corresponding to the metric name and values.

If you implement some metrics, please consider contributing them to this project.