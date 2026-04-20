# write a program to check a palindrome or not
# Example :-      madam      racecar    

# METHOD :- 1     USING SLICING  
text = "racecar"

if text == text[::-1]:
    print("THIS IS A PALINDROME")
else:
    print("THIS IS NOT A PALINDROME") 









#METHOD :- 2  USING LOOP
text = "madam"
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text
    
if reversed_text == text:
    print("This is Palindrome")
else:
    print("This is not a Palindrome")