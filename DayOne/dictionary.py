#dic in python used for storing key value pairs
#key value pair is called as item
#key is unique and value can be duplicate

#creating a dictionary
#using curly braces
person = {"name":"John", "age":30, "city":"New York"}
if person.get("job"):
    print(person.get("job"))
else:
    print("No job found")


#update dictionary
person.update({"job":"Engineer"})
print(person)

#delete item from dictionary
# del person["job"]
# print(person)

#delete all items from dictionary
# person.clear()
# print(person)


for key ,value in person.items():
    print(f"{key} : {value}")