# Write a program to find the second larget number in the array 

arr = [24, 45, 120, 90 , 99, 56, 40, 34, 68]

largest = -1
second_largest = -1

for i in arr:
    if largest < i:
        second_largest = largest
        largest  = i
    elif second_largest < i and largest != i:
        second_largest = i;


print("the largest number is : ", largest)
print("the second largest number is : ", second_largest)







