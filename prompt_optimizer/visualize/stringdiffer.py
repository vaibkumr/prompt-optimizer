from difflib import ndiff


class StringDiffer:
    def __init__(self):
        """
        Initializes a StringDiffer object with the original and optimized strings.
        """
        pass

    def __call__(self, original: str, optimized: str) -> None:
        """
        Prints the visualized difference between the original and optimized strings.
        Deletions are shown in red, insertions in green, and unchanged parts in default color.

        Args:
            original (str): The original string.
            optimized (str): The optimized string.
        """
        original = str(original)
        optimized = str(optimized)

        diff = list(ndiff(original, optimized))
        output = ""
        for op, _, value in diff:
            if op == "-":
                output += f"\033[91m{value}\033[0m"  # Red color for deletions
            elif op == "+":
                output += f"\033[92m{value}\033[0m"  # Green color for insertions
            else:
                output += value
        print(output)
