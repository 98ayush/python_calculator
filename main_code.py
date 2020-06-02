import math
def addition():
    a=int(input("enter the first number "))
    b=int(input("enter the second number "))
    c=a+b
    print("your addition is "+str(c))
def sub():
    a=int(input("enter the first number "))
    b=int(input("enter the second number "))
    c=a-b
    print("your Substraction is "+str(c))
def mul():
    a=int(input("enter the first number "))
    b=int(input("enter the second number "))
    c=a*b
    print("your Multiplication is "+str(c))
def div():
    a=int(input("enter the first number "))
    b=int(input("enter the second number "))
    c=a/b
    print("your Division is "+str(c))
def simple():
    p=int(input("enter the principle amount "))
    r=int(input("enter the rate of interest "))
    t=int(input("enter the time in years "))
    s=(p*r*t)/100
    print("Your simple interest for "+str(t)+" years is "+str(s))
def compound():
    p=int(input("enter the principle amount "))
    r=int(input("enter the rate of interest "))
    t=int(input("enter the time in years "))
    a=p*math.pow((1+(r/100)),t)
    print("your total amount after "+str(t)+" years of compound interest is "+str(a))
    c=a-p
    print("compound interest after" +str(t)+" years is "+str(c))
    
def calci():
    print("Welcome to Finance Calculator World")
    print("  1.Addition  ")
    print("  2.Substraction  ")
    print("  3.Multiplication  ")
    print("  4.Dvision  ")
    print("  5.Simple Interest  ")
    print("  6.Compound interest  ")
    value=int(input("Enter your your between 1-6  "))
    if value==1:
        addition()
    elif value==2:
        sub()
    elif value==3:
        mul()
    elif value==4:
        div()
    elif value==5:
        simple()
    elif value==6:
        compound()
    else:
        print("please enter value betwwen 1-6")
        calci()


print("welcome")
calci()


def calci():
    print("Welcome to Finance Calculator World")
    print("  1.Addition  ")
    print("  2.Substraction  ")
    print("  3.Multiplication  ")
    print("  4.Dvision  ")
    print("  5.Simple Interest  ")
    print("  6.Compound interest  ")
    value=int(input("Enter your your between 1-6  "))
    if value==1:
        addition()
    elif value==2:
        sub()
    elif value==3:
        mul()
    elif value==4:
        div()
    elif value==5:
        simple()
    elif value==6:
        compound()
    else:
        print("please enter value betwwen 1-6")
        calci()


print("Thanks for using calculator")
