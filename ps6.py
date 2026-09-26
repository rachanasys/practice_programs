# Write a python program to Calculate surface area of a Cylinder
import math
radius = 3
height = 10
cylinder_surface_area = (2 * math.pi * radius * height) + (2 * math.pi * (radius ** 2))
print("Total surface area of the cylinder:", round(cylinder_surface_area, 2))
