arr = [1, 2, 4, 5]


n = len(arr) + 1         # total length 5              


total_sum = n * (n + 1) // 2
arr_sum = sum(arr)
missing = total_sum - arr_sum

arr.append(missing)
arr.sort()


print(arr)
