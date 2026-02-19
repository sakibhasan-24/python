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



#Logical Operators

# and, or, not
# and - both conditions must be true
# or - either one of the conditions must be true
# not - reverse the result
# True and True = True
# True and False = False
# False and True = False
# False and False = False


role =input("Enter your role: (admin, user, guest) ")
isAccessCard=True
userExperience=4

if role =="admin" and isAccessCard and userExperience>3:
    print ("Welcome admin")
    print("You can apply for project Manager...........")
elif role =="user" and isAccessCard and userExperience>2:
    print ("Welcome user")
    print("You can apply for developer...........")
elif role =="guest" and isAccessCard and userExperience>1:
    print ("Welcome guest")
    print("You can apply for tester...........")


isLoggedIn=False

if not isLoggedIn:
    print("Please login to continue")