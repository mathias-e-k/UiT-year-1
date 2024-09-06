# This program creates a Car object, a Truck object,
# and an SUV object.
import vehicles
import pickle
import os.path
# Constants for the menu choices
NEW_CAR_CHOICE = 1
NEW_TRUCK_CHOICE = 2
NEW_SUV_CHOICE = 3
FIND_VEHICLE_CHOICE = 4
SHOW_VEHICLES_CHOICE = 5
QUIT_CHOICE = 6

FILE_PATH = "data.pickle"


def main():
    vehicles_list = []
    if os.path.isfile(FILE_PATH):
        file = open(FILE_PATH, "rb")
        while True:
            try:
                vehicles_list.append(pickle.load(file))
            except EOFError:
                break
            except pickle.UnpicklingError:
                print("Error: There was an issue while reading from file.")
                break
    else:
        print("File not found, new save file will be created in current directory on exit")

    choice = 0
    while choice != QUIT_CHOICE:
        # display the menu.
        display_menu()

        # Get the user's choice.
        try:    
            choice = int(input('Enter your choice: '))
        except ValueError:
            choice = 0
            print("Error: Choice has to be a number")
            continue

        # Perform the selected action.
        if choice == NEW_CAR_CHOICE:
            print('Input car data:')
            try:
                make = input("Make: ")
                year = int(input("Year: "))
                milage = int(input("Milage: "))
                price = float(input("Price: "))
                doors = int(input("Doors: "))
                car = vehicles.Car(make, year, milage, price, doors)
            except ValueError as ex:
                print("Error: Invalid data:", ex)
                continue
            vehicles_list.append(car)

        elif choice == NEW_TRUCK_CHOICE:
            print('Input truck data:')
            try:
                make = input("Make: ")
                year = int(input("Year: "))
                milage = int(input("Milage: "))
                price = float(input("Price: "))
                drivetype = input("Drivetype: ")
                truck = vehicles.Truck(make, year, milage, price, drivetype)
            except ValueError as ex:
                print("Error: Invalid data:", ex)
                continue
            vehicles_list.append(truck)

        elif choice == NEW_SUV_CHOICE:
            print('Input SUV data:')
            try:
                make = input("Make: ")
                year = int(input("Year: "))
                milage = int(input("Milage: "))
                price = float(input("Price: "))
                passenger_capacity = int(input("Passenger capacity: "))
                suv = vehicles.SUV(make, year, milage, price, passenger_capacity)
            except ValueError as ex:
                print("Error: Invalid data:", ex)
                continue
            vehicles_list.append(suv)

        elif choice == FIND_VEHICLE_CHOICE:
            make = input("Input make: ")
            specific_make_list = [vehicle for vehicle in vehicles_list if make in vehicle.get_make()]
            for item in specific_make_list:
                print(item)
        elif choice == SHOW_VEHICLES_CHOICE:
            #show all vehicles
            print('The following cars are in inventory:')
            for item in vehicles_list:
                print(item)

        elif choice == QUIT_CHOICE:
            with open(FILE_PATH, "wb") as file:
                for vehicle in vehicles_list:
                    pickle.dump(vehicle, file)
            print('Exiting the program...')    
        else:
            print('Error: invalid selection.')    

# The display_menu function displays a menu.
def display_menu():
    print('        MENU')
    print('1) New car')
    print('2) New truck')
    print('3) New SUV')
    print('4) Find vehicles by make')
    print('5) Show all vehicles')
    print('6) Quit')     

# Call the main function.
if __name__ == '__main__':
      main()