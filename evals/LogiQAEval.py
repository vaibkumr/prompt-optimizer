from OAIEvalManager import OaiEvalManager
import os
import utils
from prompt_optimizer.poptim import *
import compute_metric
import make_errors

class LogiQAEval(OaiEvalManager):
    def __init__(self,p_optimizer=None):
        super().__init__()
        self.reg_path = "/opt/homebrew/lib/python3.11/site-packages/evals/registry/"
        self.p_optimizer = p_optimizer
        self.samples_dir_name = "logiqa"
        self.samples_file_name = "logiqa.jsonl"
        self.optimized_samples_file_name = "temp.jsonl"
        self.eval = "temp"
        self.completion_fn = "gpt-3.5-turbo"

    def optimize_prompt(self,samples,exp_name="Default"):
        for json_data in samples:
            if exp_name in ["Autocorrect_Optim", "AutocorrectOptim"]:
                json_data["input"] = make_errors.run(json_data["input"])
            if self.p_optimizer is not None:
                temp = self.p_optimizer(json_data["input"], skip_system=False, json=True)
                json_data["input"] = temp.content
        return samples

    def get_samples_and_set_paths(self, exp_name, n_samples_max=1):
        samples_dir = os.path.join(self.reg_path,"data/", self.samples_dir_name)
        samples_path = os.path.join(samples_dir, self.samples_file_name)
        opti_samples_path = os.path.join(samples_dir, self.optimized_samples_file_name)
        registry_path = os.path.join(self.reg_path, "evals/")
        opti_registry_path = os.path.join(registry_path, self.optimized_samples_file_name)

        new_yaml = {
            "temp": {"id": "temp.dev.v0", 
                     "metrics": ["accuracy"]
                     }, #this can be changed as needed
            "temp.dev.v0": {
                "class": "evals.elsuite.basic.match:Match",
                "args": {"samples_jsonl": opti_samples_path},
            },
        }
        
        utils.write_yaml(new_yaml, opti_registry_path)
        
        samples = utils.read_jsonl(samples_path)[:n_samples_max]

        res_dir = "results/"
        res_path = os.path.join(res_dir, f"{exp_name}.jsonl")
        log_dir = "logs/"
        log_path = os.path.join(log_dir, f"{exp_name}.jsonl")
        print(samples)
        print("------------------")
        samples = self.optimize_prompt(samples, exp_name)
        print(samples)
        
        utils.write_jsonl(samples, opti_samples_path)

        tokens_opti_metric = compute_metric.token_metric(samples_path, opti_samples_path,n_samples_max)
        self.record_path = res_path
        self.log_path = log_path

        self.execute()
        
        for line in utils.read_jsonl(res_path):
            if "final_report" in line:
                accuracy = line["final_report"]["accuracy"]
                break

        results = {
            "name": exp_name,
            "tokens_opti_metric": tokens_opti_metric,
            "accuracy": accuracy,
        }
        print(results)
        utils.save_results(results, "results.csv")

if __name__ == "__main__":
    config = {
        "exp_name": "EntropyOptim",
        "n_samples_max": 10,
    }
    manager = LogiQAEval(EntropyOptim(p=0.25))
    manager.get_samples_and_set_paths(**config)
