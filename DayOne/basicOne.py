print("restart a new journey to check a person's avility")

# variable


name ="Sakib"
age = 35
isMale = True
height = 5.11
weight = 70.5

print(name,age,isMale,height,weight)

# type casting

print(type(name))
print(type(age))
print(type(isMale))
print(type(height))
print(type(weight))


# input
# input always return a string

favouriteFood = input("Enter your food item : ")
print("Your favourite food is : ",favouriteFood)
print("Your favourite food is : " + favouriteFood)
print("Your favourite food is : " + favouriteFood + " and your age is : " + str(age))



# Exercise 1

# rectangle area calculated

length = float(input("Enter the length of rectangle : "))
breadth = float(input("Enter the breadth of rectangle : "))
area = length * breadth
print("The area of rectangle is : ",area)



# string

strValue=input("Enter a string (favourite programming language): ")
print("Your favourite programming language is : ",strValue)
print(f"Your favourite programming language length  is : {len(strValue)}")



#logical 

mark=87

if mark <80 :
    print("You are fail")
else:
    print("You are pass")





#exercise 2
# Even or Odd


checkNumber=int(input("Enter a number : "))

if checkNumber % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


import math
print(math.pi)