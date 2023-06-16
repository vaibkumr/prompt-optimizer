import os
import random
import string
import openai
from prompt_optimizer.poptim import StopWordOptim
from prompt_optimizer.wrapper.sql_db import SQLDBManager
from prompt_optimizer.wrapper.openai import OpenAIWrapper
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_sample_db():
    p_optimizer = StopWordOptim(verbose=True)
    sql_db = SQLDBManager("sample_project", "/Users/vaibkumr/Documents/sample.db")
    oai_wrapper = OpenAIWrapper(sql_db, p_optimizer)
    n = 100
    for i in range(n):
        x = random.choice(string.ascii_letters)
        response = oai_wrapper(
            openai.ChatCompletion.create,
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "user", "content": f"Generate some text following the character: {x}"},
                ]
        )
        print(f"{[i]/[n]} {response}")



if __name__ == "__main__":
    generate_sample_db()