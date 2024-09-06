def reverse(num: int) -> int:
    if num < 10:
        return num
    return reverse(num // 10) + (num % 10) * pow(10, len(str(num))-1)

def reverse_display(num) -> None:
    print(reverse(int(num)))

number = input("Enter an integer: ")
reverse_display(number)
