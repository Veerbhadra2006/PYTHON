from array import *

arr = array("i", [])

n = int(input("Enter the number: "))

for i in range(n):
    arr.append(int(input("Enter the next input: ")))

# printing outside loop
for x in arr:
    print(x, end=" ")