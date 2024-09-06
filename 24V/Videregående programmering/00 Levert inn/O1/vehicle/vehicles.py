class Vehicle:
    def __init__(self, make, year, milage, price) -> None:
        self._make = make
        self._year = year
        self._milage = milage
        self._price = price
    
    def get_make(self):
        return self._make

    def __str__(self) -> str:
        return f"{self._make}, Year: {self._year}, Milage: {self._milage}, Price: {self._price}"

class Car(Vehicle):
    def __init__(self, make, year, milage, price, doors) -> None:
        super().__init__(make, year, milage, price)
        self._doors = doors
    
    def __str__(self) -> str:
        return super().__str__() + f", Doors: {self._doors}"

class Truck(Vehicle):
    def __init__(self, make, year, milage, price, drivetype) -> None:
        super().__init__(make, year, milage, price)
        self._drivetype = drivetype
    
    def __str__(self) -> str:
        return super().__str__() + f", Drivetype: {self._drivetype}"

class SUV(Vehicle):
    def __init__(self, make, year, milage, price, passenger_capacity) -> None:
        super().__init__(make, year, milage, price)
        self._passenger_capacity = passenger_capacity
    
    def __str__(self) -> str:
        return super().__str__() + f", Number of passengers: {self._passenger_capacity}"
