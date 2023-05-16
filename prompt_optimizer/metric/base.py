from abc import ABC, abstractmethod


class Metric(ABC):
    def __init__(self):
        self.key = None

    @abstractmethod
    def run(self, prompt_before, prompt_after):
        pass

    def run_json(self, json_data_before, json_data_after):
        res = self.run(json_data_before["content"], json_data_after["content"])
        return res

    def batch_run(self, prompts_before, prompts_after, skip_system=False, json=True):
        avg_m = 0
        n = 0
        for pb, pa in zip(prompts_before, prompts_after):
            if json:
                if skip_system and pb["role"] == "system":
                    continue
                else:
                    avg_m += self.run_json(pb, pa)[self.key]
                    n += 1
            else:
                avg_m += self.run(pb, pa)[self.key]
                n += 1
        return avg_m / n

    def __call__(self, prompt_before, prompt_after):
        return self.run(prompt_before, prompt_after)
