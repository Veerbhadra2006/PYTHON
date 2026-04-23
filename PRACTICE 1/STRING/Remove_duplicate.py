# write a program to remove the duplicates from the string

text = "Hello world"

result = " "

for char in text:
    if char not in result:
        result +=char
print("String after removing duplicates : ", result)