from datetime import datetime


class Flight:
    def __init__(self, flight_number: str, departure: datetime, arrival: datetime) -> None:
        self.__flight_number = flight_number
        self.__departure_time = departure
        self.__arrival_time = arrival

    def get_flight_number(self) -> str:
        return self.__flight_number
    
    def set_departure_time(self, value):
        self.__departure_time = value

    def get_departure_time(self) -> datetime:
        return self.__departure_time
    
    def set_arrival_time(self, value):
        self.__arrival_time = value

    def get_arrival_time(self) -> datetime:
        return self.__arrival_time
    
    def get_flight_time(self) -> int:
        total_time = self.__arrival_time - self.__departure_time
        minutes = total_time.days*24*60 + total_time.seconds // 60
        return minutes


class Itinerary:
    def __init__(self, flights: list) -> None:
        self.__flights = flights
        self.__flights.sort(key=Flight.get_departure_time)

    def get_total_flight_time(self) -> int:
        return sum(flight.get_flight_time() for flight in self.__flights)

    def get_total_travel_time(self) -> int:
        departure = self.__flights[0].get_departure_time()
        arrival = self.__flights[-1].get_arrival_time()
        total_time = arrival - departure
        minutes = total_time.days*24*60 + total_time.seconds // 60
        return minutes







def main():

    flights = []

    flights.append(Flight("US230",

        datetime(2014, 4, 5, 5, 5, 0),

        datetime(2014, 4, 5, 6, 15, 0)))

    flights.append(Flight("US235",

        datetime(2014, 4, 5, 6, 55, 0),

        datetime(2014, 4, 5, 7, 45, 0)))

    flights.append(Flight("US237",

        datetime(2014, 4, 5, 9, 35, 0),

        datetime(2014, 4, 5, 12, 55, 0)))

   

    itinerary = Itinerary(flights)

    print(itinerary.get_total_travel_time())

    print(itinerary.get_total_flight_time())

if __name__ == "__main__":
    main()