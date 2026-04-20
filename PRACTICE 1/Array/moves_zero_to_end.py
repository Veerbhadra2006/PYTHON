# write a program to moves zeros to end of the array

arr = [10, 0, 20, 30, 0, 40, 50]

insert_pos = 0

# moves non zero elements to the front. (keeping) their order
for x in arr:
    if x != 0:
        arr[insert_pos] = x 
        insert_pos +=1
        
# Fill the remaining position with zeros
for i in range(insert_pos, len(arr)):
    arr[i] = 0
    
print(arr)