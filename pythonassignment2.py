#Write a Python program to convert kilometers to miles?

km = float(input("enter the kilometers"))
conv_fac = 0.621371
miles = km * conv_fac
print("the %0.2f is equal to %0.2f miles" %(km , miles))

#Write a Python program to convert Celsius to Fahrenheit?

celsius = float(input("enter the celsius"))
fahrenheit = celsius * 1.8 + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))

#Write a Python program to display calendar?

import calendar
print(calendar.calendar(2022))

Write a Python program to solve quadratic equation?
ax^2 + bx + c = 0
2x^2 - 5x + 6 = 0
a = 2,b=-5,c = 6
b^2-4ac >= 0
(x-3)(x-2)=0
x^2-5x+6 = 0
a = 1, b=-5 c = 6
25-24 = 1>0


x = (-b+(b2-4ac)^0.5)/2a
x = (-b-(b2-4ac)^0.5)/2a

x = (-(-5)+(1)0.5)/2 = (5+1)/2 = 3
x = (-(-5)-(1)0.5)/2 = (5-1)/2 = 2

import math

a = int(input("enter value of a "))
b = int(input("enter value of b "))
c = int(input("enter value of c "))

sol = (b*b)-(4*a*c)
if sol<0:
    print("Solution doesn't exist")
else:
    x1 = (-b+math.sqrt(sol))/(2*a)
    x2 = (-b-math.sqrt(sol))/(2*a)
    print(x1)
    print(x2)


#Write a Python program to swap two variables without temp variable?

x=int(input("enter first number"))
y=int(input("enter second number"))
x,y=y,x
print("value of first number", x)
print("value of second number", y)


