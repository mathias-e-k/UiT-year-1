from photobox import list_speeders
from speed_ticket import Speed_ticket
import vehicles

import pickle
import os.path

NEW_CAR_CHOICE = 1
NEW_TRUCK_CHOICE = 2
NEW_SUV_CHOICE = 3
FIND_VEHICLE_CHOICE = 4
SHOW_VEHICLES_CHOICE = 5
CHECK_SPEED_VIOLATIONS_CHOICE = 6
QUIT_CHOICE = 7

FILE_PATH = "data.pkl"


def main():
    vehicles_list = []
    if os.path.isfile(FILE_PATH):
        get_vehicles_from_file(vehicles_list, FILE_PATH)
    else:
        print("File not found. You may be running this program in the wrong directory..." )
        print("New save file will be created in current directory on exit.")

    choice = 0
    while choice != QUIT_CHOICE:
        display_menu()
        choice = input('Enter your choice: ')
        choice = int(choice) if choice.isdigit() else 0

        if choice == NEW_CAR_CHOICE:
            make_car(vehicles_list)

        elif choice == NEW_TRUCK_CHOICE:
            make_truck(vehicles_list)

        elif choice == NEW_SUV_CHOICE:
            make_suv(vehicles_list)

        elif choice == FIND_VEHICLE_CHOICE:
            find_vehicles(vehicles_list)

        elif choice == SHOW_VEHICLES_CHOICE:
            show_all_vehicles(vehicles_list)
        
        elif choice == CHECK_SPEED_VIOLATIONS_CHOICE:
            check_speed_violations(vehicles_list)

        elif choice == QUIT_CHOICE:
            save_vehicles_to_file(vehicles_list, FILE_PATH)

        else:
            print('\nError: invalid selection.')    

    print('Exiting the program...')


def display_menu():
    print('\n        MENU')
    print('1) New car')
    print('2) New truck')
    print('3) New SUV')
    print('4) Find vehicles by make')
    print('5) Show all vehicles')
    print('6) Check speed violations')
    print('7) Quit')     


def make_car(vehicle_storage: list):
    print('\nInput car data:')
    try:
        make = input("Make: ")
        year = int(input("Year: "))
        milage = int(input("Milage: "))
        price = float(input("Price: "))
        doors = int(input("Doors: "))
        registration_number = input("Registration number: ")
        car = vehicles.Car(make, year, milage, price, registration_number, doors)
        vehicle_storage.append(car)
    except ValueError as ex:
        print("Error: Invalid data:", ex)


def make_truck(vehicle_storage: list):
    print('\nInput truck data:')
    try:
        make = input("Make: ")
        year = int(input("Year: "))
        milage = int(input("Milage: "))
        price = float(input("Price: "))
        drivetype = input("Drivetype: ")
        registration_number = input("Registration number: ")
        truck = vehicles.Truck(make, year, milage, price, registration_number, drivetype)
        vehicle_storage.append(truck)
    except ValueError as ex:
        print("Error: Invalid data:", ex)


def make_suv(vehicle_storage: list):
    print('\nInput SUV data:')
    try:
        make = input("Make: ")
        year = int(input("Year: "))
        milage = int(input("Milage: "))
        price = float(input("Price: "))
        passenger_capacity = int(input("Passenger capacity: "))
        registration_number = input("Registration number: ")
        suv = vehicles.SUV(make, year, milage, price, registration_number, passenger_capacity)
        vehicle_storage.append(suv)
    except ValueError as ex:
        print("Error: Invalid data:", ex)


def find_vehicles(vehicle_storage: list):
    make = input("\nInput make: ")
    specific_make_list = [vehicle for vehicle in vehicle_storage if make in vehicle.get_make()]
    if not specific_make_list:
        print("No vehicles found")
    for item in specific_make_list:
        print(item)


def show_all_vehicles(vehicle_storage: list):
    print('\nThe following cars are in inventory:')
    if not vehicle_storage:
        print("No vehicles found")
    for item in vehicle_storage:
        print(item)


def check_speed_violations(vehicle_storage: list):
    FILE_PATH_BOX_A = "photobox/box_a.txt"
    FILE_PATH_BOX_B = "photobox/box_b.txt"
    SPEED_LIMIT_KPH = 60
    DISTANCE_KM = 5
    try:
        speeders = list_speeders(FILE_PATH_BOX_A, FILE_PATH_BOX_B, SPEED_LIMIT_KPH, DISTANCE_KM)
    except FileNotFoundError:
        print("Error: Photobox file not found. You may be running this program in the wrong directory.")
        return
    tickets_registered = 0
    for vehicle in vehicle_storage:
        registration = vehicle.get_registration()
        if registration not in speeders:
            continue
        average_speed_kph, datetime = speeders[registration]
        ticket = Speed_ticket(registration, datetime, average_speed_kph, SPEED_LIMIT_KPH)
        tickets_registered += vehicle.register_ticket(ticket)
    if tickets_registered > 0:
        print(f"\nRegistered {tickets_registered} new tickets.")
    else:
        print("\nNo new tickets found.")


def get_vehicles_from_file(vehicle_storage: list, filename: str):
    file = open(filename, "rb")
    while True:
        try:
            vehicle_storage.append(pickle.load(file))
        except EOFError:
            break
        except pickle.UnpicklingError:
            print("Error: There was an issue while reading from file.")
            break


def save_vehicles_to_file(vehicle_storage: list, filename: str):
    vehicle_storage.sort(key=str)
    with open(filename, "wb") as file:
        for vehicle in vehicle_storage:
            pickle.dump(vehicle, file) 


if __name__ == '__main__':
      main()