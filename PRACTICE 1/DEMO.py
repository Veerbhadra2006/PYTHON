# write a program to check a string 1 rotatin of string 2

string1 = "abcde"

string2 = "cdeab"

# step1 length check 
if len(string1) != len(string2):
    print("No, rotation nahi hai")
else:
    temp = string1 + string1
    
#step2 check substring
if string2 in temp:
    print("Yes, rotation hai")
else:
    print("No, rotation nahi hai")