import math


class Rectangle2D:
    def __init__(self, x: float = 0, y: float = 0, width: float = 0, height: float = 0) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def set_center_x(self, x: float) -> None:
        self.x = x

    def set_center_y(self, y: float) -> None:
        self.y = y

    def get_center_x(self) -> float:
        return self.x

    def get_center_y(self) -> float:
        return self.y

    def get_width(self) -> float:
        return self.width

    def get_height(self) -> float:
        return self.height

    def get_area(self) -> float:
        return self.width * self.height

    def get_perimeter(self) -> float:
        return 2 * self.width + 2 * self.height

    def contains_point(self, x: float, y: float) -> bool:
        distance_x = math.sqrt((x - self.x) ** 2)
        distance_y = math.sqrt((y - self.y) ** 2)
        if distance_x <= self.width / 2 and distance_y <= self.height / 2:
            return True
        else:
            return False

    def contains(self, rectangle) -> bool:
        x = rectangle.get_center_x()
        y = rectangle.get_center_y()
        width = rectangle.get_width()
        height = rectangle.get_height()
        contains_x = self.x + self.width / 2 >= x + width / 2 and self.x - self.width / 2 <= x - width / 2
        contains_y = self.y + self.height / 2 >= y + height / 2 and self.y - self.height / 2 <= y - height / 2
        if contains_x and contains_y:
            return True
        else:
            return False

    def overlaps(self, rectangle) -> bool:
        x = rectangle.get_center_x()
        y = rectangle.get_center_y()
        distance_x = math.sqrt((x - self.x) ** 2)
        distance_y = math.sqrt((y - self.y) ** 2)
        width = rectangle.get_width()
        height = rectangle.get_height()
        overlaps_x = distance_x - (self.width / 2 + width / 2) < 0
        overlaps_y = distance_y - (self.height / 2 + height / 2) < 0
        if overlaps_x and overlaps_y:
            return True
        else:
            return False

    def __contains__(self, other) -> bool:
        x = other.get_center_x()
        y = other.get_center_y()
        width = other.get_width()
        height = other.get_height()
        contains_x = self.x + self.width / 2 <= x + width / 2 and self.x - self.width / 2 >= x - width / 2
        contains_y = self.y + self.height / 2 <= y + height / 2 and self.y - self.height / 2 >= y - height / 2
        if contains_x and contains_y:
            return True
        else:
            return False

    def __cmp__(self, other):
        # __cmp__ is not longer supported in python 3
        a = self.get_area()
        b = other.get_area()
        return (a > b) - (a < b)

    def __lt__(self, other) -> bool:
        return self.get_area() < other.get_area()

    def __le__(self, other) -> bool:
        return self.get_area() <= other.get_area()

    def __eq__(self, other) -> bool:
        return self.get_area() == other.get_area()

    def __ne__(self, other) -> bool:
        return self.get_area() != other.get_area()

    def __gt__(self, other) -> bool:
        return self.get_area() > other.get_area()

    def __ge__(self, other) -> bool:
        return self.get_area() >= other.get_area()
