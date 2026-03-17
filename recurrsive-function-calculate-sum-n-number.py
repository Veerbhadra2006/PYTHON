def call_sum(n):
    sum = 0;
    for i in range(1,n+1):
        sum += i
    return sum;
    
result = call_sum(5)

print(result)