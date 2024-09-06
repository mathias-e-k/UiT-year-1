isbn_9_digits = input("Pick the first 9 digits to generate an ISBN-10: ")
if len(isbn_9_digits) != 9 or not isbn_9_digits.isdigit():
    print("You did not enter the correct amount of digits, or you used invalid characters..")
    quit()

sum = 0
for i in range(1, 10):
    sum += int(isbn_9_digits[i-1]) * i
checksum = str(sum % 11)
if checksum == "10": 
    checksum = "X"

print(f"Your ISBN-10 is {isbn_9_digits + checksum}")
