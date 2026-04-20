# write a program to count a even and odd number

arr = [24, 45, 32, 12, 98, 33, 20, 5, 40, 31]

evenCounter = 0
oddCounter = 0 

for i in arr:
    if i % 2 == 0:
        evenCounter = evenCounter + 1
    else:
        oddCounter = oddCounter + 1
    
print("Total even number is : ", evenCounter)

print("Total odd number is : ", oddCounter)