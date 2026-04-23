# write a program to check a string 1 rotation of string2 

string1 = "abcde"
string2 = "cdeab"

if len(string1) != len(string2):
    print("Rotation can't allowed")
    
temp = string1 + string1

if string2 in temp:
    print("Yes, String1 is rotation of string2")
else:
    print("No, string1 can't rotation of string2")