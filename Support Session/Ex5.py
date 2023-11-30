import math
from random import randint as ran
def menu():
    print("Menu:\n1-Triangle Area\n2-Volume of prism\n3-Circle Area\n4-Lotto\n5-Message\n6-exit")
    opt = int(input())
    if opt in range(1,7):
        return opt

def message():
    print("Welcome Back. Don't ever give up. Merry Christmas")

def triarea(b=2,h=2):
    area = 0.5*b*h
    return area

def triprism(b, h, l):
    v = triarea(b,h)*l
    return v

def circarea(r):
    area = math.pi * r**2
    return area

def lotto():
    for i in range(6):
        print(ran(1,59), end="\t")

def main():
    while True:
        x = menu()
        if x == 6:
            break
        elif x == 1:
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            t_a = triarea(b, h)
            print(f"Area of this triangle is {t_a}")
        elif x == 2:
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            length = float(input("Enter length of prism: "))
            print(f"Volume of the prism is {triprism(base, height, length)}")
        elif x == 3:
            radius = float(input("Enter radius: "))
            print(f"Area of the circle is {circarea(radius)}")
        elif x == 4:
            lotto()
        elif x == 5:
            message()


# x = triarea(1,2) + triarea(10,5) + triarea()
# print(f"Total area is {x}cm^2")