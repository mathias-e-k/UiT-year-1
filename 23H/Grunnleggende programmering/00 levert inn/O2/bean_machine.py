import random
def drop_ball(slots: int) -> int:
    ball_path = ""
    ball_position = 0
    for i in range(slots-1):
        direction = random.choice(["Left", "Right"])
        if direction == "Right":
            ball_path += "R"
            ball_position += 1
        else:
            ball_path += "L"
    print(ball_path)
    return ball_position


def draw_triangle(slots: int):
    padding = slots - 1
    nails = 1
    print(" " * padding + "| |")
    while padding > 0:
        padding -= 1
        print(" " * padding + "/ " + "● " * nails + "\\")
        nails += 1


def draw_results(results: list):
    height = max(results) + 1
    for x in range(height-1):
        row = "|"
        for y in results:
            if y >= height - x:
                row += "O|"
            else:
                row += " |"
        print(row)
    
    row = "|"
    for y in results:
        if y >= 1:
            row += "O\u0332|"
        else:
            row += "_|"
    print(row)


if __name__ == "__main__":
    number_of_balls = int(input("Enter the number of balls to drop: "))
    number_of_slots = int(input("Enter the number of slots: "))
    slot_counter = [0 for _ in range(number_of_slots)]
    print(slot_counter)
    for ball in range(number_of_balls):
        slot_counter[drop_ball(number_of_slots)] += 1
    print(slot_counter)
    draw_triangle(number_of_slots)
    draw_results(slot_counter)

