# write a program to count a vowels and consonants

text = "AEGHOPKLMN"

vowels = ""
consonants = ""

for char in text:
    if char in "AEIOU":
        vowels = vowels + char
    else:
        consonants = consonants + char

print("vowels :-", vowels)
print("consonants :-", consonants)