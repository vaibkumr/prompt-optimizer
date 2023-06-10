import os
import json
import yaml
import subprocess
import csv
import os

# Most of the code here is written by chatgpt


def dataframe_to_markdown(df, md_path):
    markdown = "| " + " | ".join(df.columns) + " |\n"
    markdown += "| " + " | ".join(["---"] * len(df.columns)) + " |\n"

    for _, row in df.iterrows():
        markdown += "| " + " | ".join(str(value) for value in row) + " |\n"

    with open(md_path, "w") as handle:
        handle.write(markdown)

    return markdown


def save_results(dictionary, file_path):
    file_exists = os.path.isfile(file_path)

    with open(file_path, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=dictionary.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(dictionary)


def read_yaml(file_path):
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)
    return data


def write_yaml(data, file_path):
    with open(file_path, "w") as file:
        yaml.dump(data, file)


def read_jsonl(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
        json_list = []
        for line in lines:
            json_obj = json.loads(line)
            json_list.append(json_obj)
    return json_list


def write_jsonl(data, file_path):
    with open(file_path, "w") as f:
        for obj in data:
            f.write(json.dumps(obj) + "\n")


def run_bash(bash_command):
    process = subprocess.Popen(bash_command, shell=True)
    process.wait()
