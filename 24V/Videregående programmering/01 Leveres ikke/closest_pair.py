import random
import math
import time

def closest_pairBF(points: list):
    point_a = (-math.inf, -math.inf)
    point_b = (math.inf, math.inf)
    current_distance = math.dist(point_a, point_b)
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            new_distance = math.dist(points[i], points[j])
            if new_distance < current_distance:
                current_distance = new_distance
                point_a = points[i]
                point_b = points[j]
    return point_a, point_b


def closest_pair(points: list):
    points = sorted(points)
    points_ordered_on_y = sorted(points, key=lambda x: (x[1], x[0]))
    return closest_pair_helper(points, points_ordered_on_y)

def closest_pair_helper(points, pointsY):
    if len(points) == 2:
        return math.dist(points[0], points[1])
    if len(points) == 3:
        return min(math.dist(points[0], points[1]), math.dist(points[1], points[2]), math.dist(points[2], points[0]))
    
    # divide
    mid = len(points) // 2
    mid_point = points[mid]
    left_points = points[ : mid]
    right_points = points[mid : ]
    leftY = [p for p in pointsY if p[0] <= mid_point[0]]
    rightY = [p for p in pointsY if p[0] > mid_point[0]]
    left_distance = closest_pair_helper(left_points, leftY)
    right_distance = closest_pair_helper(right_points, rightY)
    shortest_distance = min(left_distance, right_distance)

    # combine
    mid_x = points[mid][0]
    left, right = mid_x - shortest_distance, mid_x + shortest_distance
    strip = [p for p in pointsY if p[0] >= left and p[0] <= right]
    size = len(strip)
    for i in range(size):
        for j in range(i+1, size):
            if math.dist(strip[i], strip[j]) > shortest_distance:
                break
            if math.dist(strip[i], strip[j]) < shortest_distance:
                shortest_distance = math.dist(strip[i], strip[j])

    return shortest_distance

if __name__ == "__main__":
    a, b = 0, 500000
    NUMBER_OF_POINTS = 50000
    points = [(random.randint(a, b), random.randint(a, b)) for _ in range(NUMBER_OF_POINTS)]

    # start_time = time.time()
    # p1, p2 = closest_pairBF(points)
    # print(math.dist(p1, p2))
    # print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    print(closest_pair(points))
    print("--- %s seconds ---" % (time.time() - start_time))
