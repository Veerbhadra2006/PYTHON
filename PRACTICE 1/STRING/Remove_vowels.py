# Write a program to Remove the vowels

text = "ABCDEFGHIJKLMNOPQRSTUVWZYZ"

string = ""

for char in text:
    if char not in "AEIOU":
        string = string + char
        
print("After Removing the vowels : ", string)