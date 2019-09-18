import math

HALF_MAX = 65504.0
HALF_MIN = 6.10352e-5

def log10(x):
    return math.log10(x)

def pow(x, y):
    return math.pow(x, y)

def pow10(x):
    return math.pow(10.0, x)

def dot_f3_f3(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def mult_f3_f33(a, m):
    x = a[0] * m[0][0] + a[1] * m[1][0] + a[2] * m[2][0]
    y = a[0] * m[0][1] + a[1] * m[1][1] + a[2] * m[2][1]
    z = a[0] * m[0][2] + a[1] * m[1][2] + a[2] * m[2][2]
    return [x, y, z]
