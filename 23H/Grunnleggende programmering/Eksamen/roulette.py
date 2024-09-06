# koden fungerer som forventet
def play_roulette(num: int) -> str:
    output = ""
    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    # pay 0
    if num == 37:
        return "P0"
    # pay 00
    if num == 38:
        return "P00"
    if num > 38 or num < 1:
        return "ERR"
    # pay <tall>
    output += f"P{num:02d}"
    # pay black
    if num in black:
        output += " PB"
    # pay red
    if num in red:
        output += " PR"
    # pay odd
    if num % 2 == 1:
        output += " PO"
    # pay even
    if num % 2 == 0:
        output += " PE"
    # pay 1-18
    if num <= 18:
        output += " P1-18"
    # pay 19-36
    if num > 18:
        output += " P19-36"
    return output



if __name__ == "__main__":
    print(play_roulette(16))
