#Conditional Statements 
#if,elif,else(SYNTAX)
age = 44

if(age<=34):
    print("Not allowed")

elif(age >=34):
    print("Most Welcome")

# Light
light = "pink"

if( light == "blue"):
    print("GO")
elif(light == "green"):
    print("stop")
elif(light == "Yellow"):
    print("Look")
else:
    print("Light is broken")

#Marks >= 90, Grade="A"
#90> marks>=80, Grade="B"
#80> marks>=70, Grade="C"
#70>marks,Grade="D"

marks = int(input("Enter Your Mark:"))

if(marks >=90):
    Grade="A"

elif(marks < 90 and marks >=80):
    Grade="B"
elif(marks < 80 and marks >=70):
    Grade="C"
else:
    Grade = "Poor"

print("The Grade of the student is -->", Grade)

#NESTING

age = 45

if(age >=18):
    if(age>=80):
        print("Cannot Drive")
    else:
        print("Can drive")

#Test :

Num = int(input("Enter the number:"))

if(Num % 2 == 0):
    number = "Even"
else:
    number = "Odd"

print("The NUmber is :" , number)


#Find the greatest of three number entered by the user
a=int(input("Enter number:"))
b=int(input("Enter number:"))
c=int(input("Enter number"))

if(a>b and a>c):
    print("a is the largest")
elif(b>a and b>c):
    print("b is the largest")
elif(c>a and c>b):
    print("c is the largest")

# write a code to check if the number is multiple of 7 or not

x = int(input("Enter the number:"))

if (x % 7 == 0):
    y =("Multiple of 7")
else:
    y =("Not a multiple of 7")

print("The NUmber is:", y)