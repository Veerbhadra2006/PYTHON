# write a program to find the first non -repeating char

string = "payyyaaarii"

unique = " "

for char in string:
    if string.count(char) == 1:
        unique = unique + char

print("The unique character is : ",unique)
    
        