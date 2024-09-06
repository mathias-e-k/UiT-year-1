def format(seconds):
    hour = (seconds % 86400) // 3600
    minute = (seconds % 3600) // 60
    second = seconds % 60
    return f"{hour:02d}:{minute:02d}:{second:02d}"


if __name__ == "__main__":
    user_input = int(input("Enter total seconds: "))
    time = format(user_input)
    print(f"The hours, minutes, and seconds for total seconds {user_input} is {time}")
