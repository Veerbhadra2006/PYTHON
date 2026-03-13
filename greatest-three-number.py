num1 = int(input("Enter the number1: "));
num2 = int(input("Enter the number2 : "));
num3 = int(input("Enter the number3 : "));

if (num1 > num2 and num1 > num3):
    print(f"num1 : {num1} is greatest");
    
elif(num2 > num1 and num2 > num3):
    print(f"num2 : {num2} is greatest")
    
else:
    print(f"num3 : {num3} is greatest")