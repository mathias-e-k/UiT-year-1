import random


class Point:
    def __init__(self, name, x, y) -> None:
        self.x = x
        self.y = y
        self.name = name
    

    def __str__(self) -> str:
        return f"{self.name}: {self.x} {self.y}"


def right_side_of_line(p0, p1, p2):
    return (p1.x - p0.x) * (p2.y - p0.y) - (p2.x - p0.x) * (p1.y - p0.y) < 0


def convex_hull(points: list) -> list:
    # gift wrapping algorithm
    hull = []
    h0 = points[0]
    for point in points:
        if point.x > h0.x:
            h0 = point
        elif point.x >= h0.x and point.y < h0.y:
            h0 = point
    hull.append(h0)
    t0 = h0
    while True:
        t1 = points[0] if points[0] != t0 else points[1]
        for point in points:
            if right_side_of_line(t0, t1, point):
                t1 = point
        if t1 == h0:
            break
        hull.append(t1)
        t0 = t1
    return hull


if __name__ == "__main__":
    points = [Point("A", 5, 2), Point("B", 15, 3), Point("C", 16, 7), Point("D", 14, 7), Point("E", 13, 8), 
            Point("F", 3, 8), Point("G", 2, 5), Point("H", 7, 7), Point("I", 5, 6), Point("J", 10, 4)]
    random.shuffle(points)
    # convex hull: A-B-C-E-F-G
    hull = convex_hull(points)
    for point in hull:
        print(point)
    

