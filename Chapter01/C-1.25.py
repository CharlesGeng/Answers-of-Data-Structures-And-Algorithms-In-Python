# Write a short Python function that takes a string s, representing a sentence,
# and returns a copy of the string with all punctuation removed. For exam-
# ple, if given the string "Let s try, Mike.", this function would return
# "Lets try Mike".

import string


def remove_ponctuations(text: str) -> str:
    result = ''
    for c in text:
        if c not in string.punctuation:
            result += c
    return result


print(remove_ponctuations("Let's try, Mike."))
