# SLICING - LAST 3 NUMBER NOT INCLUDE IN THE ARRAY

import array 

val = array.array("i",[23,24,25,26,27,28,29,30,31,32,33,34,35])

a = val[0 : -3];

for x in a:
    print(x, end=" ")