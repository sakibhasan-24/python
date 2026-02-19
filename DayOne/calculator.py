# let's create a simple calculator

# assume we don't know anything about function

numOne =float(input("Enter first number: "))
numTwo =float(input("Enter second number: "))
op=input("Enter operator: (+,-,*,/) ")

if op=="+":
    print(numOne+numTwo)
elif op=="-":
    print(numOne-numTwo)
elif op=="*":
    print(numOne*numTwo)
elif op=="/":
    print(numOne/numTwo)
else:
    print("Invalid operator")