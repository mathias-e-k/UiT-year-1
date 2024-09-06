def palindrome(num):
    string = str(num)
    for i in range(len(string) // 2):
        if string[i] != string[-(1+i)]:
            return False
    return True


if __name__ == '__main__':
    number = int(input("Skriv inn ett tall ->"))
    if palindrome(number):
        print(f'Tallet {number} er ett palindromtall')
    else:
        print (f'Tallet {number} er ikke ett palindromtall')
