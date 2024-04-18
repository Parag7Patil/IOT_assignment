#face and place value


a=int(input("enter th value "))
m=0
while(a!=0):
    rem=a%10
    m=m*10+rem
    a=a/10
    
print(m)
