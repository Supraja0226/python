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
    
#checking if a number is positive, negative or zero
num=int(input("enter a number:"))
if(num>0):
    print("num is a positive number")
elif(num<0):
    print("num is a negative number")
else:
    print("num is zero")
    
#checking the given user alphabet vowels or constant
alphabet=input("enter a alphabet:")
if alphabet in ('a','e','i','o','u'):
    print("vowel")
else:
    print("not a vowel")
    
#checking the person valid voter or not
age=int(input("enter your age:"))
if(age>=18):
    print("valid voter")
else:
    print("not a valid voter")
#weather suggestion based on temperature 
temp=int(input("enter the temperature:"))
if(temp>40):
    print("it's too hot")
elif(temp>30 and temp<40):
    print("it's hot")
elif(temp>20 and temp<30):
    print("it's warm")
else:
    print("it's cold") 
    
#check if a number is greater than 0
num=int(input("enter any number:"))
if(num>0):
    print("num is greater than 0")
else:
    print("num is less than or equal to 0")