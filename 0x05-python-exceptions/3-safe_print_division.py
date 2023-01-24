#!/usr/bin/python3
def safe_print_division(a, b):
    k = 0
    try:
        k = a / b
        return k
    except ZeroDivisionError:
        return None 
    finally:
        print("Inside result: {}".format(k))
