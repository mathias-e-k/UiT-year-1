decimal_input = int(input("Enter a decimal number between 0 and 15: ")) 
while decimal_input not in list(range(0,16)):
    print("Your number is not between 0 and 15.")
    decimal_input = int(input("Enter a decimal number between 0 and 15: "))
decimal = decimal_input
binary_string = ""

if decimal >= 8:
    binary_string += "1"
    decimal -= 8
else: 
    binary_string += "0"

if decimal >= 4:
    binary_string += "1"
    decimal -= 4
else: 
    binary_string += "0"

if decimal >= 2:
    binary_string += "1"
    decimal -= 2
else: 
    binary_string += "0"

if decimal >= 1:
    binary_string += "1"
    decimal -= 1
else: 
    binary_string += "0"

print(f"The binary number for {decimal_input} is {int(binary_string)}")

