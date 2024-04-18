# maximum out of three number 
 
num1=int(input("enter the  number1 "))
num2=int(input("enter the number 2 "))
num3=int(input("enter the number 3 "))

def function(num1,num2,num3):

    if num1>num2 and num1>num3: 
        print("number 1 is greater ")

    elif num2>num1 and num2>num3:
        print("the number 2 is greater ")

    elif num3>num1 and num3>num2:
        print("the number 3 is greater ")

function(num1,num2,num3)