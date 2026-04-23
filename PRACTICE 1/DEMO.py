# write a program to convert a case
text = input("Enter a string : ")

print('\n choose a conversion')
print("1. UPPERCASE")
print("2. lowercase")
print("3 . Title case")
print("4. Swap Case (toogle)")
print("5. Sentence case")

choice = input("Enter choice 1 - 5 : ").strip()
#strip() use because i help to remove extra space of starting  and ending of the space
if choice == "1":
    result = text.upper()
elif choice == "2":
    result = text.lower()
elif choice == "3":
    result = text.title()
elif choice == "4":
    result = text.swapcase()
elif choice == "5":
    result = text[:1].upper() + text[1:].lower()
else:
    print("Invalid choice, please choose ka right option")
    raise SystemExit


print(result)    
    
    
    
    
    
    