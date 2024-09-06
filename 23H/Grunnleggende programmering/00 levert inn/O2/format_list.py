def format_list(list_of_items):
    formatted_string = ""
    if len(list_of_items) > 1:
        formatted_string += "The items are "
    else:
        formatted_string += "The item is "
    
    while len(list_of_items) > 0:
        formatted_string += f"{list_of_items.pop(0)}"
        if len(list_of_items) > 1:
            formatted_string += ", "
        elif len(list_of_items) == 1:
            formatted_string += " and "

    return formatted_string


if __name__ == "__main__":
    items = []
    while True:
        user_input = input("Enter an item (blank to quit): ")
        if user_input == "":
            break
        items.append(user_input)
    if items:
        print(format_list(items))
    else:
        print("You did not write any items")
