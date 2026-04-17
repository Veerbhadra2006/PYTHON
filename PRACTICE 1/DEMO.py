# write a program to remove the duplicates elements from the array

arr = [90, 80, 70, 10, 60, 50, 20, 40, 30,       10, 70, 60]

unique_arr = list(set(arr));

print(unique_arr);

        
    
# ====================================================================================    
 
    
# create a using loop
unique_arr = []

for i in arr:
    if i not in unique_arr:
        unique_arr.append(i)

print(unique_arr)