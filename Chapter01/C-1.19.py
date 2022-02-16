# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [ 'a' , 'b' , 'c' , ..., 'z' ], but without having to type all 26 such
# characters literally.

# 'a' == 97
print(list(chr(97 + i) for i in range(26)))
