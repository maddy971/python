''''A=10
B=20.12
C=23.9876
D="Hello"
to know what type of value stored in variables
print(type(A))
print(type(B))
print(type(C))
print(type(D))
print("Addition of numbers : ",A+B)
print("Multiplication of numbers : ",A*B)

a = input("Enter your Number")
print("Your Number ",a)
b = input("Enter your Name")
print("Your Name ",b)

<WAP to read two numbers and find the sum of those two numbers>

a = int(input("Enter a number: "))
b = int(input("Entr b number: "))
print("Addition of a and b : ",a+b)'''

# <WAP to read two numbers and find greatest of them>
# a = int(input("Enter A number: "))
# b = int(input("Enter B number: "))
# if a>b:
#     print("A is greater")
# else:
#     print("B is greater")

# 1) +ve and -ve
# a = int(input("Enter any number: "))
# if a > 0 :
#     print("The given number is positive")
# else :
#     print("The given number id Negative")

# a = int(input("Enter any number: "))
#
# if a % 2 ==0:
#     print("The number is even")
# else:
#     print("The number is odd")

# a = int(input("Enter a year: "))
# if a%4==0 or a%100==0:
#     print("The given year is leap year")
# else:
#     print("The given year not a leap year")

# a= int(input("Enter a number: "))
# if a%5==0:
#     print(a," is divisible by 5 ")
# else:
#     print(a," is not divisible by 5 ")

'''a = int(input("Enter any 1st number: "))
b = int(input("Enter any 2nd number: "))
c = int(input("Enter any 3rd number: "))
if a>b and a>c :
    print("1st number is big")
elif b>c :
    print("2nd number is big")
else:
    print("3rd number is big")

for i in range(1,30,1):
    if(i%3==0 and i%5==0):
        print(i,"= Madu Basti oni")
    elif(i%3 == 0):
        print(i,"= Madu")
    elif(i%5==0):
        print(i,"= Basti oni")
    else :
        print(i)

num=int(input("Enter a number"))
i=1
while(i<=10):
     print(i*num)
     i=i+1

# Reverse of number

num=int(input("Enter any number: "))
temp=0
# sum=0
rev=0
while(num>0):
    temp=num%10
    # print("Reverse of a number: ", temp)
    rev=rev*10+temp
    # sum=sum+temp
    num=num//10

# print("Sum of that number: ",sum)
print("Reverse of a number: ",rev)

# String class in python
str1="java"
str2="PYTHON"
str3="madu"
str4="madu"
str5="Welcome to Django"
print(len(str1))
print(str1.lower())
print(str2.isupper())
print(str1.islower())
print(str3.__eq__(str4))
print(str1.upper())
print(str2.lower())
print(str5.count("e"))
print(str3.startswith("m"))
print(str3.endswith("v"))
print(str4.capitalize())'''

# Math Class in Python

import math
print(math.ceil(5.2))
print(math.fabs(-4))
print(math.pow(5,2))
print(math.trunc(5.9))
print(math.sqrt(49))
# print(math.isqrt(64))

str1="java"
str2="python"
str3="wel come to django"
print(str1[0])
print(str3[2:6])
print(str2[4:])
print(str3[:6])
