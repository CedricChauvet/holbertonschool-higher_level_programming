#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number = str(number)[-1]
if int(last_number) > 5:
    than = "and is greater than 5"
elif int(last_number) < 6:
    than = "and is less than 6"
if int(last_number) == 0:
    is_0 = "and is 0"
else:
    is_0 = "and not 0"
print("Last digit of", number, "is", last_number, than, is_0)
