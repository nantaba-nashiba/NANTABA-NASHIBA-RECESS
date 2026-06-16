import math

def circle_area(radius):
    return math.pi * radius ** 2

radius = float(input("Enter radius: "))
area = circle_area(radius)
print(f"Area: {area:.2f}")
