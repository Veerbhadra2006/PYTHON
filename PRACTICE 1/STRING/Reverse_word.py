# write a program to reverse a word

# METHOD : 1 ---- SLICING
text = input("Enter a word : ")

reverse = text[: : -1]

print("The Reversed String is : ", reverse)





# METHOD : 3  ---- USING LOOP
text = input("Enter a words : ")

reverse = ""
for char in text:
    reverse = char + reverse

print("Reversed word : ", reverse)