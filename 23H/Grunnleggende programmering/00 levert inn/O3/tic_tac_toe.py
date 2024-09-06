def main():
    turn_number = 1
    player = "X"
    board = create_board()

    while True:
        draw_board(board)

        if turn_number > 9:
            print("no winner")
            break

        if turn_number % 2 == 1:
            player = "X"
        else:
            player = "O"

        prompt_player(board, player)

        if is_winner(board, player):
            draw_board(board)
            print(f"{player} player won")
            break

        turn_number += 1


def create_board() -> list:
    BOARD_SIZE = 3
    board = []
    for _ in range(BOARD_SIZE):
        board.append([" " for _ in range(BOARD_SIZE)])
    return board


def draw_board(board: list) -> None:
    for row in board:
        print("-------------")
        print(f"| {row[0]} | {row[1]} | {row[2]} |")
    print("-------------")


def prompt_player(board: list, player: str) -> None:
    while True:
        input_row = int(input(f"Enter a row for player {player}: "))
        input_column = int(input(f"Enter a column for player {player}: "))
        if board[input_row][input_column] == " ":
            board[input_row][input_column] = player
            return
        else:
            print("This cell is already occupied. Try a different cell")


def is_winner(board: list, player: str) -> bool:
    # horizontal -
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True

    # vertical |
    for i in range(len(board)):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    # diagonal \ /
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


if __name__ == "__main__":
    main()
    
