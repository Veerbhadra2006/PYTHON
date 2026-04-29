seen = set()
added = set()
duplicates = []

for x in arr:
    if x in seen and x not in added:
        duplicates.append(x)
        added.add(x)
    else:
        seen.add(x)
        
print(duplicates)
