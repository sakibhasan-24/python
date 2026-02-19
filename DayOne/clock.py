# # let's create a digital timer

import time
myTime = int(input("Enter the number of seconds : "))

while myTime >0:
    seconds = myTime % 60
    minutes = myTime // 60
    hours= myTime // 3600
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    myTime -=1
print("Time's up")
