import numpy as np
import torch
from transformers import AutoModelForMaskedLM, AutoTokenizer

from prompt_optimizer.poptim.base import PromptOptimize


class EntropyOptim(PromptOptimize):
    def __init__(
        self,
        model_name="bert-base-cased",
        p=0.9,
        verbose=False,
        metrics=[],
    ):
        """Higher p = Larger Cutoff"""
        super().__init__(verbose, metrics)
        self.p = p * 100
        self.model_name = model_name
        self.load_mlm_model_tokenizer()

    def load_mlm_model_tokenizer(self):
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForMaskedLM.from_pretrained(self.model_name)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def generate_confidence_values(self, sentence):
        inputs = self.tokenizer.encode_plus(
            sentence, return_tensors="pt", add_special_tokens=False
        )
        input_ids = inputs["input_ids"].to(self.device)
        attention_mask = inputs["attention_mask"].to(self.device)

        with torch.no_grad():
            outputs = self.model(input_ids, attention_mask=attention_mask)
            logits = outputs.logits[0]

        probs = torch.softmax(logits, dim=-1)
        entropy_mapping = []
        for i, input_id in enumerate(input_ids[0].detach().numpy()):
            entropy = -torch.log2(probs[i, input_id]).detach().item()
            entropy_mapping.append((input_id, entropy))
        return entropy_mapping

    def percentile_cutoff_tokens(self, entropy_mapping):
        """select the most informative/surprising tokens"""
        surprise_cutoff = np.percentile([cm[1] for cm in entropy_mapping], self.p)
        filtered_tokens = [cm[0] for cm in entropy_mapping if cm[1] >= surprise_cutoff]
        return filtered_tokens

    def run_chunk(self, prompt):
        entropy_mapping = self.generate_confidence_values(prompt)
        filtered_tokens = self.percentile_cutoff_tokens(entropy_mapping)
        optimized_prompt = self.tokenizer.decode(filtered_tokens)
        return optimized_prompt

    def run(self, prompt):
        max_l = int(0.7 * self.model.config.max_position_embeddings)
        tokens = prompt.split()
        opti_prompt = ""
        for idx in range(0, len(tokens), max_l):
            part_prompt = " ".join(tokens[idx : idx + max_l])
            part_opti_prompt = self.run_chunk(part_prompt)
            opti_prompt += part_opti_prompt
        return opti_prompt
