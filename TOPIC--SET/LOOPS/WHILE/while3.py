# print the multiplication table for number n 

num = int(input("Enter the number for table : "))

i = 1
while(i <= 10):
    result = num * i
    print(f"{num} * {i} = {result}")
    i+=1