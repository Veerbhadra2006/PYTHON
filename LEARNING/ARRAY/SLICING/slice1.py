# SLICING - IF YOU WANT TO SOME AMOUNT OF DATA IN WHOLE ARRAY

import array
val = array.array("i", [1,2,3,4,5,6,7,8,9])

a = val[2:5]

for x in a:
    print(x, end=" ")