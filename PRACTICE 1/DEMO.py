# write a program to Reverse a word 

# METHOD : 1
text = input("Enter a word : ")

reverse = text[: : -1]

print("The Reversed String is : ", reverse)




# METHOD : 2
text = input("Enter a word : ")
reverse = ""

for char in text:
    reverse  = char + reverse

print("The Reversed string is ; ", reverse)