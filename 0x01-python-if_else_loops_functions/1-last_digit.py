#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

stringNumber = repr(number)

if number < 0:
    lastDigitString = '-' + stringNumber[-1]
else:
    lastDigitString = stringNumber[-1]

lastDigit = int(lastDigitString)

print(f"Last digit of {number} is {lastDigit}", end='', sep='', flush=True)

if lastDigit == 0:
    print(" and is 0")
elif lastDigit < 6:
    print(" and is less than 6 and not 0")
elif lastDigit > 5:
    print(" and is greater than 5")
