# # let's create a flyover car passing system using class and instance variable

# from datetime import datetime
# class CrossingSystem:
#     # class variable
#     total_cars = 0

#     def __init__(self, name):
#         # instance variable
#         self.name = name
#         self.cars = []
#         # increment the total_cars by 1
#         CrossingSystem.total_cars += 1

#     def add_car(self, car):
#         self.cars.append(car)


# # create two crossing system
# crossing1 = CrossingSystem("mustaz crossing, dhaka, bangladesh,car no:QWERTY")
# crossing2 = CrossingSystem("mustaz crossing, dhaka, bangladesh,car no:ASDFGH")
# crossing3 = CrossingSystem("mustaz crossing, dhaka, bangladesh,car no:ZXCVBN")

# # CrossingSystem.total_cars=0

# print(f"{crossing1.total_cars} total car crossing till {datetime.now()}")



# make it profesonal


from datetime import datetime

class FlyoverGate:
    # Class variable (Private-ish approach using underscore)
    _total_cars_count = 0 

    def __init__(self, gate_location):
        self.gate_location = gate_location
        # Instance variable: Stores specific cars of THIS gate
        self.passed_cars_list = []

    def record_entry(self, car_number):
       
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        car_data = {"plate": car_number, "time": timestamp}
        
        self.passed_cars_list.append(car_data)
        FlyoverGate._total_cars_count += 1
        
        print(f"[ENTRY] Car {car_number} passed through {self.gate_location} at {timestamp}")

    def get_local_count(self):
        return len(self.passed_cars_list)


    
    @classmethod    
    def get_total_system_count(cls):
        print(f"Total cars crossed: {cls}")
        return cls._total_cars_count

       

banani_gate = FlyoverGate("Banani Crossing, Dhaka")
kuril_gate = FlyoverGate("Kuril Flyover, Dhaka")


banani_gate.record_entry("DHK-METRO-1234")
banani_gate.record_entry("DHK-METRO-5678")
kuril_gate.record_entry("DHK-METRO-9999")

print("-" * 30)
print(f"Total cars at Banani Gate: {banani_gate.get_local_count()}")
print(f"Total cars at Kuril Gate: {kuril_gate.get_local_count()}")
print(f"Global Count (Total Cars): {FlyoverGate.get_total_system_count()}")