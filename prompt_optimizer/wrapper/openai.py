import json
import time
from typing import Any, Callable, Dict

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

        start_time = time.time()
        response = openai_func(*args, **kwargs) #TODO: Also log errors
        request_runtime = time.time() - start_time

        prompt_before_token_count = self.token_count(messages_before)
        prompt_after_token_count = response["usage"]["prompt_tokens"]
        continuation_token_count = response["usage"]["completion_tokens"]

        if self.db_manager:
            with self.db_manager:
                self.db_manager.add(
                    [
                        timestamp,
                        json.dumps(messages_before),
                        json.dumps(optimized_messages),
                        json.dumps(response.choices[0]),
                        prompt_before_token_count,
                        prompt_after_token_count,
                        continuation_token_count,
                        model,
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
