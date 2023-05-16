import random


def introduce_spelling_errors(sentence, error_rate=0.079):
    """according to grammarly, people make 7.9 errors per 100 words"""
    words = sentence.split()
    num_errors = int(len(words) * error_rate)
    for _ in range(num_errors):
        word_index = random.randint(0, len(words) - 1)
        word = words[word_index]
        char_index = random.randint(0, len(word) - 1)
        new_char = random.choice(
            [chr(i) for i in range(97, 123)]
        )  # Random lowercase letter
        words[word_index] = word[:char_index] + new_char + word[char_index + 1 :]
    return " ".join(words)


def run(json_data, error_rate=0.079):
    for json_string in json_data:
        json_string["content"] = introduce_spelling_errors(
            json_string["content"], error_rate
        )
    return json_data


# sentence = "This is a sample sentence for testing."
# error_rate = 0.079
# result = introduce_spelling_errors(sentence, error_rate)
# print(result)
