from speed_ticket import Speed_ticket

class Vehicle:
    def __init__(self, make, year, milage, price, registration_number) -> None:
        self._make = make
        self._year = year
        self._milage = milage
        self._price = price
        self._registration_number = registration_number
        self._speed_tickets = {}
    
    def get_make(self):
        return self._make
    
    def get_registration(self):
        return self._registration_number
    
    def register_ticket(self, ticket) -> int:
        '''Registers the ticket for the vehicle, returns 1 if it is a new ticket and 0 if the ticket was already registered.'''

        if ticket.get_registration() != self._registration_number:
            raise Exception("Ticket registration is not equal to vehicle registration")
        if ticket.get_time() in self._speed_tickets:
            print(f"Speed ticket: {str(ticket)}")
        else:
            self._speed_tickets[ticket.get_time()] = ticket
            print(f"Registered new speeding ticket: {str(ticket)}")
            return 1
        return 0

    def __str__(self) -> str:
        return f"{self._make}, Year: {self._year}, Registration: {self._registration_number}, Milage: {self._milage}, Price: {self._price}"

class Car(Vehicle):
    def __init__(self, make, year, milage, price, registration_number, doors) -> None:
        super().__init__(make, year, milage, price, registration_number)
        self._doors = doors
    
    def __str__(self) -> str:
        return super().__str__() + f", Doors: {self._doors}"

class Truck(Vehicle):
    def __init__(self, make, year, milage, price, registration_number, drivetype) -> None:
        super().__init__(make, year, milage, price, registration_number)
        self._drivetype = drivetype
    
    def __str__(self) -> str:
        return super().__str__() + f", Drivetype: {self._drivetype}"

class SUV(Vehicle):
    def __init__(self, make, year, milage, price, registration_number, passenger_capacity) -> None:
        super().__init__(make, year, milage, price, registration_number)
        self._passenger_capacity = passenger_capacity
    
    def __str__(self) -> str:
        return super().__str__() + f", Number of passengers: {self._passenger_capacity}"
