# search for a number x in this tuple using Loop
# nums=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x = 36
count = 0

while count < len(nums):
    if nums[count] == x:
        print(f"item found at index: {count}")
        break
    count += 1

      