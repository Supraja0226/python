light="red"

if(light=="green"):
    print("Go")
elif(light=="yellow"):
    print("look")
elif(light=="red"):
    print("stop")
else:
    print("light is broken")
    
    
age=20

if(age>=18):
    print("can vote")
else:
    print("cannot vote")
    
#Grade students based on marks
marks=int(input("Enter marks:"))

if(marks>=90):
    print("grade A")
elif(marks>=80 and marks<90):
    print("grade B")
elif(marks>=70 and marks<80):
    print("grade C")
elif(marks>=60 and marks<70):
    print("grade D")
else:
    print("grade F")
    
#nesting if statements 
age=int(input("enter your age:"))

if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")
    
#check if a number entered is odd or even
num=int(input("Enter a number:"))

if(num%2==0):
    print("even number")
elif(num%2!=0):
    print("odd number")
else:
    print("not a number") 
    
#finding the largest number among three numbeers
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))

if(num1>num2 and num1>num3):
    print("num1 is the largest number")
elif(num2>num1 and num2>num3):
    print("num2 is the largest number")
elif(num3>num1 and num3>num2):
    print("num3 is the largest number")
else:
    print("all the the numbers are equal")
    
#checking if a number is multiple of 7 or not
num=int(input("enter a number:"))
if(num%7==0):
     print("multiple of 7")
else:
    print("not a multiple of 7")