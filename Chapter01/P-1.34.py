# A common punishment for school children is to write out a sentence mul-
# tiple times. Write a Python stand-alone program that will write out the
# following sentence one hundred times: “I will never spam my friends
# again.” Your program should number each of the sentences and it should
# make eight different random-looking typos.

import random

sentence = 'I will never spam my friends again.'
max_index = len(sentence) - 1

# Generate 8 time errors
err_list = random.sample(range(100), 8)

counter = 0

while counter < 100:
    # Generate Error
    if counter in err_list:
        i = -1
        while not str.isalpha(sentence[i]):
            i = random.randint(0, max_index)
        c = sentence[i]
        while c == sentence[i]:
            c = chr(96 + random.randint(1,26))
        print(sentence[:i] + c + sentence[i+1:] + "!!TYPOS!!")
    # Print correct sentence
    else:
        print(sentence)
    counter += 1
