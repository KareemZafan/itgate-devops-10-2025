import math

def add_value(a, b):
    return (a + b)

def sub_value(a, b):
    return (a - b)

def mul_value(a, b):
    return (a * b)

def div_value(a, b):


def get_square_root(a):
    return math.sqrt(a)

def get_min_value(a , b):
    if a < b:
        return a
    else:
        return b


def get_max_value(a , b):
    if a > b:
        return a
    else:
        return b


print(get_square_root(100)) # 10.00

print(get_max_value(1,-20)) # 1

print(get_min_value(1,-20)) # -20


