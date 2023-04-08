import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

from prompt_optimizer.metric.base import Metric


class BERTScoreMetric(Metric):
    """BERTScoreMetric between the prompt and optmized prompt.

    Args:

    """

    def __init__(self):
        super().__init__()
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        self.model = AutoModelForSequenceClassification.from_pretrained(
            "bert-base-uncased", num_labels=2
        )

    def run(self, prompt_before, prompt_after):
        inputs = self.tokenizer(
            [prompt_before, prompt_after],
            return_tensors="pt",
            padding=True,
            truncation=True,
        )
        outputs = self.model(**inputs, output_hidden_states=True)
        embedding1 = outputs.hidden_states[-2][0]
        embedding2 = outputs.hidden_states[-2][1]
        cos_sim = torch.nn.functional.cosine_similarity(embedding1, embedding2)
        precision, recall, f1 = (
            cos_sim.mean().item(),
            cos_sim.max().item(),
            2
            * cos_sim.mean().item()
            * cos_sim.max().item()
            / (cos_sim.mean().item() + cos_sim.max().item()),
        )
        return {
            "bert_score_precision": precision,
            "bert_score_recall": recall,
            "bert_score_f1": f1,
        }
