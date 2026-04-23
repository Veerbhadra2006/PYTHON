# write a program to check a substring

# METHOD : 1
text = input("Enter the main string : ")
sub = input("Enter the sub string : ")

if sub in text:
    print("Sub string in present")
else:
    print("Substring is not present")



#  METHOD : 2 USING LOOP 
text = input("Enter main Strig : ")
sub = input("Enter substrig : ")

found =  False

for i in range(len(text) - len(sub) +1):
    if text[i : i+len(sub)] == sub:
        found =  True
        break

if found:
    print("Substring is presennt")
else:
    print("Substring is not present")

