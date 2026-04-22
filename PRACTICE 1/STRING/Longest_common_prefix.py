# Write a program to find the longest common prefix

arr = ["flower", "flow" , "flight"]

if not arr:
    print(" ")
    raise SystemExit

prefix = arr[0]

for word in arr[1:]:
    while prefix != "" and word.startswith(prefix) == False:
        prefix = prefix[0 : len(prefix)-1]
        
print(prefix)