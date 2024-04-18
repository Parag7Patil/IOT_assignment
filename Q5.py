#factorial

num=int(input("enter the number for factorial "))

def function(num):
    fact=1
    i=1
    while(i<=num):
        fact=fact*i
        i=i+1
    return fact
print(f"factorial of  {num} is : {function(num)}")
        
