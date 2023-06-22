import os
import openai
from prompt_optimizer.poptim import StopWordOptim
from prompt_optimizer.wrapper.sql_db import SQLDBManager
from prompt_optimizer.wrapper.openai import OpenAIWrapper
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def test_openai_wrapper():
    p_optimizer = StopWordOptim(verbose=True)
    sql_db = SQLDBManager()
    oai_wrapper = OpenAIWrapper(sql_db, p_optimizer)
    response = oai_wrapper(
        openai.ChatCompletion.create,
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Who won the world series in 2020?"},
                {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
                {"role": "user", "content": "Where was it played?"}
            ]
    )
    print(f"response: {response}")
    response = True

    assert response is not None, "Failed!"


test_openai_wrapper()