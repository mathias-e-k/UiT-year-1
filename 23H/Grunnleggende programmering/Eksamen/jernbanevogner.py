import math
# koden virker som forventet

class Railcar:
    noof_railcars_created = 0
    def __init__(self, id: str, load: int, length: int) -> None:
        self._id = id
        self._load = load
        self._length = length
        Railcar.noof_railcars_created += 1

    def get_noof_railcars_created():
        return Railcar.noof_railcars_created
    
    def __lt__(self, other):
        if self.volume() < other.volume():
            return True
        else: 
            return False
    
    def __str__(self):
        return f"id={self._id} load={self._load} length={self._length}"


class Rectangle(Railcar):
    def __init__(self, id: str, load: int, length: int, width: int, height: int) -> None:
        super().__init__(id, load, length)
        self._width = width
        self._height = height
    
    def volume(self):
        return round(self._length * self._width * self._height, 2)
    
    def __str__(self):
        return super().__str__() + f" width={self._width} height={self._height} volume={self.volume()}"

class Cylinder(Railcar):
    def __init__(self, id: str, load: int, length: int, radius: int) -> None:
        super().__init__(id, load, length)
        self._radius = radius
    
    def volume(self):
        return round(self._length * math.pi * self._radius**2, 2)
    
    def __str__(self):
        return super().__str__() + f" radius={self._radius} volume={self.volume()}"

class Sphere(Railcar):
    def __init__(self, id: str, load: int, length: int, radius: int, units: int) -> None:
        super().__init__(id, load, length)
        self._radius = radius
        self._units = units
    
    def volume(self):
        return round((4/3) * math.pi * self._radius**3 * self._units, 2)
    
    def __str__(self):
        return super().__str__() + f" radius={self._radius} units={self._units} volume={self.volume()}"


def print_all(railcars: list):
    print("Noof railcars", Railcar.get_noof_railcars_created())
    for railcar in railcars:
        print(railcar)

if __name__ == "__main__":
    rectangle = Rectangle("1001", 10, 10, 5, 5)
    cylinder = Cylinder("1002", 10, 10, 5)
    sphere = Sphere("1003", 10, 10, 3, 4)
    railcars_lst = [rectangle, cylinder, sphere]

    # Sorter på volum
    railcars_lst.sort()
    print_all(railcars_lst)

    print("")
    # Sorter på ID
    railcars_lst.sort(key=Railcar.__str__)
    print_all(railcars_lst)


    
