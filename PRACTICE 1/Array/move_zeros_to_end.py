# Write a program to move the zeros to the end of the array

arr = [0, 1, 0, 3, 12, 0, 5]

insert_pos = 0

# Move non-zero elements to the front (keeping their order)
for x in arr:
    if x != 0:
        arr[insert_pos] = x
        insert_pos += 1

# Fill the remaining positions with zeros
for i in range(insert_pos, len(arr)):
    arr[i] = 0

print(arr)
