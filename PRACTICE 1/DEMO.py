# Write a program to count the even / odd numbers

# even = 24, 32, 12, 98, 20, 40

# odd = 45, 33, 5, 31


arr = [24, 45, 32, 12, 98, 33, 20, 5, 40, 31]

evenCounter = 0
oddCounter = 0

for i in arr:
    if i % 2 == 0:
        evenCounter = evenCounter + 1
    else:
        oddCounter = oddCounter + 1
        
print("the total even number is : ", evenCounter)
print("the total odd number is  : ", oddCounter)
