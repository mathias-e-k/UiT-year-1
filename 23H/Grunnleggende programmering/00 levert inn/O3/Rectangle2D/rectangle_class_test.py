from Rectangle2D import Rectangle2D

r1_x = float(input("Enter the center x-coordinate of r1: "))
r1_y = float(input("Enter the center y-coordinate of r1: "))
r1_width = float(input("Enter the width of r1: "))
r1_height = float(input("Enter the height of r1: "))
r1 = Rectangle2D(r1_x, r1_y, r1_width, r1_height)

r2_x = float(input("Enter the center x-coordinate of r2: "))
r2_y = float(input("Enter the center y-coordinate of r2: "))
r2_width = float(input("Enter the width of r2: "))
r2_height = float(input("Enter the height of r2: "))
r2 = Rectangle2D(r2_x, r2_y, r2_width, r2_height)

print(f"Area for r1 is {r1.get_area()}")
print(f"Perimeter for r1 is {r1.get_perimeter()}")
print(f"Area for r2 is {r2.get_area()}")
print(f"Perimeter for r2 is {r2.get_perimeter()}")

print(f"r1 contains the center of r2? {r1.contains_point(r2.get_center_x(), r2.get_center_y())}")
print(f"r1 contains r2? {r1.contains(r2)}")
print(f"r2 in r1? {r2 in r1}")
print(f"r1 overlaps r2? {r1.overlaps(r2)}")
print(f"r1 < r2? {r1 < r2}")
