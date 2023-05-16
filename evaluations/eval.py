import os
import compute_metric
import utils
from prompt_optimizer.poptim import *
import make_errors


def get_samples_and_paths(n_samples_max=100):
    samples_dir = (
        "/Users/v/Documents/PromptOptimizerProj/evals/evals/registry/data/logiqa/"
    )
    samples_fname = "logiqa.jsonl"
    samples_path = os.path.join(samples_dir, samples_fname)
    opti_samples_path = os.path.join(samples_dir, "temp.jsonl")
    registry_path = "/Users/v/Documents/PromptOptimizerProj/evals/evals/registry/evals/"
    opti_registry_path = os.path.join(registry_path, "temp.yaml")

    new_yaml = {
        "temp": {"id": "temp.dev.v0", "metrics": ["accuracy"]},
        "temp.dev.v0": {
            "class": "evals.elsuite.basic.match:Match",
            "args": {"samples_jsonl": opti_samples_path},
        },
    }
    utils.write_yaml(new_yaml, opti_registry_path)
    samples = utils.read_jsonl(samples_path)[:n_samples_max]

    return samples, samples_path, opti_samples_path


def run_logiqa(exp_name, p_optimizer, n_samples_max=100):
    samples, samples_path, opti_samples_path = get_samples_and_paths(n_samples_max)

    res_dir = "results/"
    res_path = os.path.join(res_dir, f"{exp_name}.jsonl")
    log_dir = "logs/"
    log_path = os.path.join(log_dir, f"{exp_name}.jsonl")

    for json_data in samples:
        if exp_name in ["Autocorrect_Optim", "AutocorrectOptim"]:
            json_data["input"] = make_errors.run(json_data["input"])

        if p_optimizer is not None:
            json_data["input"] = p_optimizer.batch_run(
                json_data["input"], skip_system=False, json=True
            )

    # Save samples
    utils.write_jsonl(samples, opti_samples_path)

    # Compute token saved metrics
    tokens_opti_metric = compute_metric.token_metric(samples_path, opti_samples_path)

    # Compute Evals metric
    utils.run_bash(
        f"oaieval gpt-3.5-turbo temp --record_path {res_path} --log_to_file {log_path}"
    )
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

    # Save results
    utils.save_results(results, "results.csv")


if __name__ == "__main__":
    EXPERIMENTS = {
        # "Default": None,
        # "Entropy_Optim_p_0.05": EntropyOptim(p=0.05),
        # "Entropy_Optim_p_0.1": EntropyOptim(p=0.1),
        # "Entropy_Optim_p_0.25": EntropyOptim(p=0.25),
        # "Entropy_Optim_p_0.5": EntropyOptim(p=0.5),
        # "SynonymReplace_Optim_p_1.0": SynonymReplaceOptim(p=1),
        # "Lemmatizer_Optim": LemmatizerOptim(),
        # "Stemmer_Optim": StemmerOptim(),
        # "NameReplace_Optim": NameReplaceOptim(),
        # "Punctuation_Optim": PunctuationOptim(),
        # "Autocorrect_Optim": AutocorrectOptim(),
        "Pulp_Optim_p_0.05": PulpOptim(p=0.05),
        "Pulp_Optim_p_0.1": PulpOptim(p=0.1),
    }
    for exp_name in EXPERIMENTS:
        p_optimizer = EXPERIMENTS[exp_name]
        run_logiqa(exp_name, p_optimizer)
