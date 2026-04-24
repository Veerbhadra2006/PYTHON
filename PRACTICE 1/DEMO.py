# write a program to Remove the vowels

text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

string = ""


for char in text:
    if char not in "AEIOU":
        string = string + char

print("After remove the vowels : ", string)
 
 
 
 
 
        


