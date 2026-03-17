# write a program to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionary & add one by one.
# (use subject name as key and marks as value)

marks = {}

x = int(input("Enter the physics marks : "))
marks.update({"physics" : x})

y = int(input("Enter the chemistry marks : "))
marks.update({"chemistry" : y});

z = int(input("Enter the maths marks : "))
marks.update({"maths" : z})

print(marks);