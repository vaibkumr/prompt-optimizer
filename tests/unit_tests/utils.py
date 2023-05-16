import os

def load_prompt(prompt_f):
    file_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "data", prompt_f)
    )
    with open(file_path, "r") as f:
        data = f.read()
    return data