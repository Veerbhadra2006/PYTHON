# Write a program to find the intersection of an array

arr =  [12, 13, 14, 15, 16, 17, 18, 19, 20]

arr2 = [21, 22, 23, 15, 24, 25, 26, 19, 27]

intersection = []

#The common elements is : 15, 19

for x in arr:
    for y in arr2:
        if x == y:
            intersection.append(x)
            
print("The intersection of the array is : ", intersection)