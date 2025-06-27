
import sys

def add(num1,num2):
    add=num1+num2
    return add
   

def sub(num1, num2):
    sub=num1-num2
    return sub
   

def mul(num1,num2):
    mul=num1*num2
    return mul

# num1= int(sys.argv[1]) # here the argument is a string and converted as a integer
# operation=sys.argv[2]
# num2=int(sys.argv[3])

num1=float(sys.argv[1]) # here the argument is a string and converted as a float
operation=sys.argv[2]
num2=float(sys.argv[3])

if operation == "add":
    add = num1 + num2
    print(add)

if operation == "sub":
    sub = num1 - num2
    print(sub)

if operation == "mul":
    mul = num1 * num2
    print(mul)        