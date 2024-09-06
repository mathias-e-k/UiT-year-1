def is_valid_board(board):
    # Only checks the if the last row is correct 
    # because this function is only called when the last row is changed
    rows = len(board) - 1 
    for i in range(rows):
        if board[i] == board[-1]:
            return False
        if board[i] == board[-1] - rows + i:
            return False
        if board[i] == board[-1] + rows - i:
            return False
    return True


def first_solution():
    board = [-1] * 8
    row = 0
    while row <= 7:
        if board[row] < 7:
            board[row] += 1
        else:
            board[row] = -1
            row -= 1
            continue
        if is_valid_board(board[: row + 1]):
            row += 1
    return board


def count_all_solutions():
    count = 0
    board = [-1] * 8
    row = 0
    while row != -1:
        if board[row] < 7:
            board[row] += 1
        else:
            board[row] = -1
            row -= 1
            continue
        if is_valid_board(board[: row + 1]):
            row += 1
        if row == 8:
            count += 1
            row -= 1
    return count


def all_solutions_recursive(board):
    if len(board) == 8 and all(i != -1 for i in board):
        return 1
    total = 0
    next_queen_position = board.index(-1)
    for i in range(8):
        board[next_queen_position] = i
        if is_valid_board(board[: next_queen_position + 1]):
            total += all_solutions_recursive(board)
    board[next_queen_position] = -1
    return total


if __name__ == "__main__":
    print(all_solutions_recursive([-1] * 8))