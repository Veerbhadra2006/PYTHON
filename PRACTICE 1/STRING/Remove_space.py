# write a program to remove the space from the string

# 1. REMOVE ALL SPACES FROM A STRING
text = "Hello world Python"
result = text.replace(" ", "")
print(result)




# 2. REMOVE ONLY LEADING AND TRAILING SPACE
text = "    hello world "
result = text.strip()
print(result)





# 3. Remove the extra space (keep single space between words)
text = "hello   world   python "
result = " ".join(text.split())

print(result)

