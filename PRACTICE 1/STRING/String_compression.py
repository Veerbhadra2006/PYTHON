# write a program String compression

text = input("Enter a string : ")

result = ""
count = 1

for i in range(len(text)):
    if i < len(text) - 1 and text[i] == text[i + 1]:
        count = count + 1
    else:
        result = result + text[i] + str(count)
        count = 1
        
print("compressed String : ", result)