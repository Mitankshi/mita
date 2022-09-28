# #Write a Python Program to Check if a Number is Positive, Negative or Zero?
#
# a=int(input("enter the number"))
# if a>0:
#     print("the number is positive")
# elif a==0:
#     print("the number is zero")
# else:
#     print("the number is negative")
#
# #Write a Python Program to Check if a Number is Odd or Even?
#
# a=int(input("enter your number"))
# if a%2!=0:
#     print("the number is odd ")
# else:
#     print("the number is even ")
#
# #Write a Python Program to Check Leap Year?
#
# year=int(input("enter a year"))
# if year%4==0 :
#     print("this is a leap year")
# else:
#     print("this is not a leap year")

#Write a Python Program to Check Prime Number


#
# a=int(input("enter the number"))
# check = 0
# if a==0 or a==1 :
#     check=1
# for i in range(2,a):
#     if a%i==0:
#         check = 1
#         break
# if check == 1:
#     print("This is not a prime number")
# else:
#     print("This is a prime number")


# #Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

a=int(input("enter first number"))
b=int(input("enter second number"))
check = 0
if a==1:
    a=a+1
for num in range(a,b+1):
    for i in range(2,num):
        if num%i==0:
            check = 1
            break
    if check == 0:
        print(num)
    else:
        check = 0
