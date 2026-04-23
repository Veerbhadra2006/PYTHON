# write a program to remove the duplicates

text = "hello world"

result = ""

for char in  text:
    if char not in result:
        result = result + char
        
print("string after the removing the duplicates : ", result)
    