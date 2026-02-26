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


# for key ,value in person.items():
    # print(f"{key} : {value}")




students = {
    "101": {
        "name": "Rahim",
        "age": 21,
        "marks": {"math": 85, "english": 78, "cs": 90},
        "attendance": 88
    },
    "102": {
        "name": "Karim",
        "age": 22,
        "marks": {"math": 70, "english": 60, "cs": 75},
        "attendance": 72
    }
}


# access data
print(students["101"]["name"])
