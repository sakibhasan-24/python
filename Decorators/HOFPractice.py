employees = [
    {"name": "Sakib", "salary": 50000},
    {"name": "Kane", "salary": 70000},
    {"name": "Sarrrrr", "salary": 45000}
]


# Formatting their name
# filtering
# give bonus

def give_bonus(em):
    # print(em)
    return {**em,"salary": em["salary"]+(em["salary"]*0.10)}

def formatName(em):
    # print(em)
    return {**em, "name": f"Employee: {em['name']}"}


def filter_employee(em):
    return em if em["salary"] > 50000 else None


def process_employee(data,func):
    process_data=[]
    for em in data:
        result=func(em)
        if result:
            process_data.append(result)
    
    return process_data

bonus=process_employee(employees,give_bonus)
print(bonus)

formatted=process_employee(employees,formatName)
print(formatted)

filtered=process_employee(employees,filter_employee)
print(filtered)