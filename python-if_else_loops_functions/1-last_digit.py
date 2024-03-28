#!/usr/bin/python3
import numpy as np
import random
number = random.randint(-10000, 10000)
try:
    last_number =np.sign(number) * int(str(number)[-1])
    if last_number > 5:
        than = "and is greater than 5"
        print("Last digit of", number, "is", last_number, than)
    elif last_number ==0:
        print("Last digit of", number, "is", last_number, "and is 0")
    elif last_number < 6:
        than = "and is less than 6 and not 0"
        print("Last digit of", number, "is", last_number, than)

except ValueError as err:
    return "TypeError"