# write a program to check a Anagram or not

str1 = "listen"
str2 = "silent"

if sorted(str1) == sorted(str2):
    print("This is Anagram")
else:
    print("This is not Anagram")