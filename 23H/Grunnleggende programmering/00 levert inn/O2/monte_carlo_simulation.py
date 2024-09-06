import random
import math
number_of_hits = 0
NUMBER_OF_POINTS = 1000000

for _ in range(NUMBER_OF_POINTS):
    x_value = random.uniform(-1, 1)
    y_value = random.uniform(-1, 1)
    point_in_circle = math.sqrt(x_value ** 2 + y_value ** 2) <= 1
    if point_in_circle:
        number_of_hits += 1
    
pi_approximation = 4 * number_of_hits / NUMBER_OF_POINTS

print(f"There were {number_of_hits} hits in the circle")
print(f"Pi is approximately {pi_approximation}")
