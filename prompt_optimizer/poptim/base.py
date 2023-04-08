from abc import ABC, abstractmethod
from .logger import logger


class PromptOptimize(ABC):
    def __init__(self, verbose=False, metrics=[]):
        self.metrics = metrics
        self.verbose = verbose

    @abstractmethod
    def run(self, prompt):
        pass

    def __call__(self, prompt):
        opti_prompt = self.run(prompt)
        if self.verbose:
            for metric in self.metrics:
                out = metric(prompt, opti_prompt)
                for key in out:
                    logger.info(f'Metric {key}: {out[key]:.3f}') 
                    logger.info(f"Prompt Before: {prompt}")
                    logger.info(f"Prompt After: {opti_prompt}")
        return opti_prompt   
    

