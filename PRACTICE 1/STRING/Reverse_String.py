#   write a program to reverse a string 

# METTHOD :- 1  USING SLICING
name = "Rajesh Pandey"

reversed_text = name[::-1]

print(reversed_text)





# METHOD :- 2   USING LOOP
name = "Avengers"
reversed = ""

for char in name:
    reversed = char + reversed
    
print(reversed)