# Write a program to intersection of two  array  - means find the common elements that was present in both array

arr =  [12, 13, 14, 15, 16, 17, 18, 19, 20]

arr2 = [21, 22, 23, 15, 24, 25, 18, 25, 26 ]

insc= []

# common elements are : - 15, 18

for x in arr:
    for y in arr2:
        if x == y:
            insc.append(x)

print(insc)