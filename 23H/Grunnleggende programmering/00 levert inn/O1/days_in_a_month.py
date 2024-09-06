month = int(input("Enter a month: "))
while month not in [1,2,3,4,5,6,7,8,9,10,11,12]:
    print("Your number is not valid")
    month = int(input("Enter a month: "))
year = int(input("Enter a year: "))
name_of_month = ['January','February','March','April','May','June',
                 'July','August','September','October','November','December']
leap_year = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

if month in [1,3,5,7,8,10,12]:
    days_in_month = 31
elif month in [4,6,9,11]:
    days_in_month = 30
elif month == 2:
    if leap_year:
        days_in_month = 29
    else:
        days_in_month = 28
print(f"{name_of_month[month-1]} {year} has {days_in_month} days")

