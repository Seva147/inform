import math
from math import cos, log, sin, exp

x = float(input("Введите значение переменной x: "))
y = float(input("Введите значение переменной y: "))
z = float(input("Введите значение переменной z: "))

a=(x**3/2)**0.5-sin(y)
b=exp(2)/3-cos(y)+z+log(y)

print(f"получено значение функции a={a}")
print(f"получено значение функции b={b}")
