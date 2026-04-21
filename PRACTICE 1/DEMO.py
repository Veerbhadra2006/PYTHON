# write a program to check a first a First non-repeating char

def first_non_repeating(s):

    for char in s:

        if s.count(char) == 1:

            return char

    return None

text = "aabbcde"

result = first_non_repeating(text)

print("First non-repeating character:", result)
