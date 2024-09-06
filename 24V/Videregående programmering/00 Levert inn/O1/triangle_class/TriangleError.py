class TriangleError(RuntimeError):
    def __init__(self, side1, side2, side3) -> None:
        sides = [side1, side2, side3]
        sides.sort()
        self.__side1 = sides[0]
        self.__side2 = sides[1]
        self.__side3 = sides[2]

    def __str__(self) -> str:
        return f"Triangle can not exist. The sum of the two smaller side lengths: {self.__side1} and {self.__side2} has to be greater than the length of the largest side: {self.__side3}"
    
    def get_side1(self):
        return self.__side1
    
    def get_side2(self):
        return self.__side2
    
    def get_side3(self):
        return self.__side3