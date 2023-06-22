from abc import ABC, abstractmethod

# import tiktoken


class Wrapper(ABC):
    """
    Abstract base class for a wrapper.

    Attributes:
        db_manager: The database manager object.
        poptimizer: The poptimizer object.
        tokenizer: The tokenizer object.
    """

    def __init__(self, db_manager, poptimizer):
        """
        Initializes a new instance of the Wrapper class.

        Args:
            db_manager: The database manager object.
            poptimizer: The poptimizer object.
        """
        self.db_manager = db_manager
        self.poptimizer = poptimizer
        # self.tokenizer = tiktoken.get_encoding("cl100k_base")

    # def token_count(
    #     self, messages: Union[List[Dict[str, str]], str], json: bool = True
    # ) -> int:
    #     """
    #     Calculates the total token count for the given messages.

    #     Args:
    #         messages: The list of messages or a single message string.
    #         json: Indicates whether the messages are in JSON format (default: True).

    #     Returns:
    #         The total token count.

    #     Raises:
    #         TypeError: If messages is not a list or a string.
    #     """
    #     if json is True:
    #         c = sum([len(self.tokenizer.encode(m["content"])) for m in messages])
    #     elif isinstance(messages, list):
    #         c = sum([len(self.tokenizer.encode(m)) for m in messages])
    #     else:
    #         c = len(self.tokenizer.encode(messages))
    #     return c

    @abstractmethod
    def wrap(self, *args, **kwargs):
        """
        Abstract method for wrapping.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        pass
