import utils
from prompt_optimizer.metric import TokenMetric


def token_metric(before_samples_dir, after_samples_dir, n_samples_max=100):
    before = utils.read_jsonl(before_samples_dir)[:n_samples_max]
    after = utils.read_jsonl(after_samples_dir)[:n_samples_max]
    metric = TokenMetric()
    avg = 0
    for json_before, json_after in zip(before, after):
        avg += metric.batch_run(json_before["input"], json_after["input"])
    return avg / len(before)
