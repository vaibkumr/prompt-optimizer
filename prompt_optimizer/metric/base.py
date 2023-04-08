from abc import ABC, abstractmethod


class Metric(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def run(self, prompt_before, prompt_after):
        pass

    def __call__(self, prompt_before, prompt_after):
        return self.run(prompt_before, prompt_after) 