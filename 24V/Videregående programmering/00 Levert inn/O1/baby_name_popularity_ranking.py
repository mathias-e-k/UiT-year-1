import urllib.request

year = input("Enter the year: ")
if not 2000 < int(year) < 2011:
    quit("year has to be between 2001 and 2010")
gender = input("Enter the gender(M/F): ").upper()
name = input("Enter the name: ").title()
url = "https://liveexample.pearsoncmg.com/data/babynameranking" + year + ".txt"
data = urllib.request.urlopen(url)
data = data.read().decode()
data = [line.split() for line in data.splitlines() if name in line.split()]
if not data:
    print("name is not in the 1000 most popular names in", year)
    quit()


match gender:
    case "M":
        name_pos = 1
        name_data = [line for line in data if name == line[name_pos]]
        if not name_data:
            print("Name does not match specified gender")
        else:
            print(f"Boy name {name} is ranked #{name_data[0][0]} in year {year}")

    case "F":
        name_pos = 3
        name_data = [line for line in data if name == line[name_pos]]
        if not name_data:
            print("Name does not match specified gender")
        else: 
            print(f"Girl name {name} is ranked #{name_data[0][0]} in year {year}")

    case _:
        print(f"Name {name} is ranked #{data[0][0]} in year {year}")

