weight = int(input("Enter weigth in kg: "))
height = int(input("Enter heigth in cm: ")) / 100
bodyMassIndex = round(weight / height**2, 2)
print(f"Your BMI is {bodyMassIndex}.")