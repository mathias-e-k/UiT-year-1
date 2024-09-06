def palindrome3(num):
    string = str(num)
    if string [0] == string[-1]:
        return True
    else:
        return False


number = int(input("Enter a three-digit integer ->"))
if len(str(number)) == 3:

    if palindrome3(number):
        print(f'The number {number} is a palindrome number!')
    else:
        print (f'The number {number} is NOT a palindrome number!')

else:
    print('The number is not three digits long')
