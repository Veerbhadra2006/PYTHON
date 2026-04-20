# ---------------------------   write a program to reverse an array (METHOD - 1 ) ---------------------------------
#REVERSE ARRAY WITH THE HELP OF reverse built-in method

arr = [25, 45, 32, 65, 67, 45, 20, 12, 2, 4]

arr.reverse()

print(arr)
    
    
    




# ---------------------------   write a program to reverse an array (METHOD - 1 )  ---------------------------------
# REVERSE ARRAY WITH THE HELP OF slice method

arr = [25, 45, 32, 65, 67, 45, 20, 12, 2, 4]

reversed_arr = arr[::-1]
print("The reversed array is : ", reversed_arr)







# ---------------------------   write a program to reverse an array (METHOD - 3 )  ---------------------------------
#REVERSE ARRAY WITH THE HELP OF LOOP

arr = [25, 45, 32, 65, 67, 45, 20, 12, 2, 4]

reversed_arr = []

for i in range(len(arr)-1, -1, -1):
    reversed_arr.append(arr[i])
    
print("THE REVERSED ARRAY IS : ", reversed_arr)
