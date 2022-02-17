# Write a short Python function that counts the number of vowels in a given
# character string.

vowels = "aeiou"


def vowel_counter(text: str) -> int:
    result = 0
    for c in text.lower():
        if c in vowels:
            result += 1
    return result


text = "asdfghjklqewrtyuiopzcxvbnmaeiou"

print(vowel_counter(text))
