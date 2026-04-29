# write a program to check a intersectiom of the array

arr = [10, 20, 30, 40, 50]

arr2 = [60, 70, 30, 80, 50]

intersection = []

for num in arr:
    for x in arr2:
        if num == x:
            intersection.append(x)

if intersection is not 0:
    print("The intersection of the array is : ",intersection)       

else:
    print("arr not intersection of arr2")     



