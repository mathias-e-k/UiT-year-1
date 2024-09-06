from GeometricObject import GeometricObject
import math

class Triangle(GeometricObject):
    def __init__(self, side1: float = 1.0, side2: float = 1.0, side3: float = 1.0) -> None:
        if self._triangle_exists(side1, side2, side3):
            super().__init__()
            self.__side1 = side1
            self.__side2 = side2
            self.__side3 = side3
        else:
            raise ValueError("Triangle can not exist. The sum of two side lengths has to exceed the length of the third side")
    
    def _triangle_exists(self, side1, side2, side3) -> bool:
        sides = [side1, side2, side3]
        sides.sort()
        if sides[0] + sides[1] >= sides[2]:
            return True
        else:
            return False

    def get_side1(self):
        return self.__side1
    
    def get_side2(self):
        return self.__side2
    
    def get_side3(self):
        return self.__side3
    
    def get_area(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        area = math.sqrt(s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3))
        return area
    
    def get_perimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + " side2 = " + str(self.__side2) + " side3 = " + str(self.__side3) 
    


if __name__ == "__main__":
    side1 = float(input("Enter side 1: "))
    side2 = float(input("Enter side 2: "))
    side3 = float(input("Enter side 3: "))
    triangle1 = Triangle(side1, side2, side3)
    triangle1.set_color(input("Enter color: "))
    filled_input = int(input("Is the triangle filled?(1/0): "))
    if filled_input == 1:
        triangle1.set_filled(True)
    else:
        triangle1.set_filled(False)

    print(triangle1)
    print(f"Triangle area: {triangle1.get_area()}")
    print(f"Triangle perimeter: {triangle1.get_perimeter()}")
    print(f"Triangle color: {triangle1.get_color()}")
    print(f"Triangle filled: {triangle1.is_filled()}")

