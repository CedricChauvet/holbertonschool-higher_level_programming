#!/usr/bin/python3
def print_last_digit(number):
    if type(number) is int:
        last_digit = str(number)[-1]
        print("{}".format(last_digit), end="")
        return last_digit
    else:
        raise Exception('patati patata')
