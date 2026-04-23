# write a program to check a substring or not

# METHOD : 1 
text = input("Enter the string : ")
sub = input("Enter the string : ")

if sub in text:
    print("Sub string is present")
else:
    print("Substring is not present")
    
    
    
    
    
# METHOD : 2 -- USING LOOP
text = input("Enter the main String : ")
sub = input("Enter the sub string : ")

found = False

for i in range(len(text) - len(sub) + 1):
    if text[i : i+len(sub)] == sub:
        found = True
        break
    

if found:
    print("Substring is present")

else:
    print("Substring is not present")