#Q1

grade=float(input("Enter the marks "))

if grade >=0 and grade <25:
    grade1='F'
    print("Your grade is: "+grade1)

elif grade >=25 and grade < 45:
    grade1='E'
    print("Your grade is: "+grade1)

elif grade >=45 and grade < 50:
    grade1='D'
    print("Your grade is: "+grade1)

elif grade >=50 and grade < 60:
    grade1='C'
    print("Your grade is: "+grade1)

elif grade >= 60 and grade < 80:
    grade1='B'
    print("Your grade is: "+grade1)

elif grade >=80 and grade <= 100:
    grade1='A'
    print("Your grade is: "+grade1)

else:
    print("Marks not in range")


#Q2

year=int(input('Enter the year '))

if year%400==0:
    leap_year= True
elif year%100==0:
    leap_year= False
elif year%4==0:
    leap_year= True
else:
    leap_year= False

if leap_year==True:
    print('Yes',year ,'is a leap year')
else:
    print('No',year ,'is not a leap year')


#Q3

import random
x=1
y=0
while x<=10:
    num1=random.randint(1,10)
    num2=random.randint(1,10)
    product=num1*num2
    print("Question",x,"%dx%d="%(num1,num2))
    sol=int(input("Solution="))
    if sol==product:
        print("Correct")
        y+=1
    else:
        print("False")
    x+=1
print("Number of correct answers=",y)

#Q4

a=0
while a <200:
    if a%5==2 and a%6==3 and a%7==2:
        print(a)
        break
    else:
        a+=1