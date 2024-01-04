#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, mul, sub, div

    a = 10
    b = 5

    res_add = add(a, b)
    res_mul = mul(a, b)
    res_sub = sub(a, b)
    res_div = div(a, b)

    print(f'{a} + {b} = {res_add}')
    print(f'{a} * {b} = {res_mul}')
    print(f'{a} / {b} = {res_div}')
    print(f'{a} - {b} = {res_sub}')
