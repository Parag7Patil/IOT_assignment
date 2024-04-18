#grade give to the student as per grade

math=int(input("enter the marks 1 "))
sci=int(input("enter the marks 2 "))
eng=int(input("enter the marks 3 "))

# student = {'marks':math,'marks':sci,'marks':eng}

average = ((math+sci+eng)/3)
print(f"average is ={average}")

if 100>average>90:
    print("grade :A ")
elif 89>average>80:
    print("grade:B")
elif 79>average>70:
    print("Grade:C")
elif 69>average>60: 
    print("Grade:D")  
elif 59>average>0:
    print("Grade:F") 