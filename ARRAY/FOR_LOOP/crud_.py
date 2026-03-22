import array

val = array.array("i", [1,2,3,4,4,5,6,7])

val.insert(2,45)
val.append(300)
val[1] = 95

for i in range(0, len(val)):
    print(val[i], end=" ")
