import json
import time
from typing import Any, Callable, Dict

import tiktoken

from prompt_optimizer.wrapper.base import Wrapper


class OpenAIWrapper(Wrapper):
    """
    Wrapper class for OpenAI API.

    Inherits from the base Wrapper class.

    Attributes:
        db_manager: The database manager object.
        poptimizer: The poptimizer object.
    """

    def __init__(self, db_manager, poptimizer):
        """
        Initializes a new instance of the OpenAIWrapper class.

        Args:
            db_manager: The database manager object.
            poptimizer: The poptimizer object.
        """
        super().__init__(db_manager, poptimizer)

    def num_tokens_from_messages(self, messages, model="gpt-3.5-turbo-0301"):
        """
        Source: https://stackoverflow.com/a/76044069
        https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
        Returns the number of tokens used by a list of messages."""
        try:
            encoding = tiktoken.encoding_for_model(model)
        except KeyError:
            print("Warning: model not found. Using cl100k_base encoding.")
            encoding = tiktoken.get_encoding("cl100k_base")
        if model == "gpt-3.5-turbo":
            print(
                "Warning: gpt-3.5-turbo may change over time. Returning num tokens assuming gpt-3.5-turbo-0301."
            )
            return self.num_tokens_from_messages(messages, model="gpt-3.5-turbo-0301")
        elif model == "gpt-4":
            print(
                "Warning: gpt-4 may change over time. Returning num tokens assuming gpt-4-0314."
            )
            return self.num_tokens_from_messages(messages, model="gpt-4-0314")
        elif model == "gpt-3.5-turbo-0301":
            tokens_per_message = (
                4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
            )
            tokens_per_name = -1  # if there's a name, the role is omitted
        elif model == "gpt-4-0314":
            tokens_per_message = 3
            tokens_per_name = 1
        else:
            raise NotImplementedError(f"""not implemented for model {model}""")
        num_tokens = 0

        if type(messages) == "list":
            for message in messages:
                num_tokens += tokens_per_message
                for key, value in message.items():
                    num_tokens += len(encoding.encode(value))
                    if key == "name":
                        num_tokens += tokens_per_name
            num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
        elif type(messages) == "str":
            num_tokens += len(encoding.encode(messages))
        return num_tokens

    def wrap(self, openai_func: Callable[..., Any], *args, **kwargs) -> Dict[str, Any]:
        """
        Wraps the OpenAI function with additional functionality.

        Args:
            openai_func: The OpenAI function to be wrapped.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            The response from the OpenAI function.

        Raises:
            KeyError: If the 'model' or 'messages' key is missing in kwargs.
        """
        model = kwargs["model"]
        timestamp = int(time.time())
        messages_before = kwargs["messages"]

        if self.poptimizer is not None:
            start_time = time.time()
            optimized_messages = self.poptimizer.run_json(messages_before)
            optimizer_runtime = time.time() - start_time
            kwargs["messages"] = optimized_messages
        else:
            optimizer_runtime = 0
            optimized_messages = {}

        prompt_before_token_count = self.num_tokens_from_messages(messages_before)
        prompt_after_token_count = self.num_tokens_from_messages(optimized_messages)

        request_start_time = time.time()
        try:
            response = openai_func(*args, **kwargs)
            continuation_token_count = response["usage"]["completion_tokens"]
            continuation = json.dumps(response.choices[0])
            error = 0
            error_name = "None"
        except Exception as e:
            error = 1
            error_name = type(e).__name__
            continuation = "None"
            continuation_token_count = 0

        request_runtime = time.time() - request_start_time

        if self.db_manager:
            with self.db_manager:
                self.db_manager.add(
                    [
                        timestamp,
                        self.db_manager.username,
                        json.dumps(messages_before),
                        json.dumps(optimized_messages),
                        continuation,
                        prompt_before_token_count,
                        prompt_after_token_count,
                        continuation_token_count,
                        model,
                        error,
                        error_name,
                        optimizer_runtime,
                        request_runtime,
                    ]
                )
        return response

    def __call__(self, *args, **kwargs) -> Dict[str, Any]:
        """
        Calls the OpenAIWrapper instance as a function.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            The response from the OpenAI function.
        """
        return self.wrap(*args, **kwargs)
