import math

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

