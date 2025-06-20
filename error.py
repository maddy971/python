from csv import excel
from idlelib.colorizer import prog_group_name_to_tag
from logging import exception

# a=10
# b=0
#
#
# try:
#     # print(x)
#     c=a+b
#     d=a/b
# except NameError:
#     print("Variable c is not defined")
# except ZeroDivisionError:
#     print("plz enter valid input")

# try:
#     # print(x)
#     print("hello world")
# except:
#     print("something went wrong")
# else:
#     print("nothing went wrong")

x = -1

if x < 0:
    x="hello"
if not type(x) is int:
    raise TypeError("only integers are allowed")
else:
    raise Exception("Sorry, no numbers below zero")

