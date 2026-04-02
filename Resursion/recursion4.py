#reverse a string

def revstr(str):
    if len(str) == 0:
        return str
    
    return revstr(str[1:]) + str[0]

print(revstr("Rajesh"))