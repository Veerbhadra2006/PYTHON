marks = int(input("Enter the marks : "));

if(marks >=90):
    print("The student got Grade - A");

elif(marks < 90 and marks >= 80):
    print("The student got Grade - B");
    
elif(marks < 80 and marks >= 70):
    print("The student got Grade - C");
    
elif(marks > 70):
    print("The student got Grade - D");
    
else:
    print("You are Fail");