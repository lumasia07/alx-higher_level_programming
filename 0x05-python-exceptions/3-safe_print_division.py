#!/usr/bin/python3
def safe_print_division(a, b):
    quotient = None
    try:
        quotient = a / b
    except ZeroDivisionError:
        print("Division by Zero is no allowed")
    except Exception as e:
        print("An expected error occured:", e)
    finally:
        print("Inside result: {}".format(quotient))

    return quotient
