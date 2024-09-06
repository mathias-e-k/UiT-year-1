class EQ:
    def __init__(self, queens: list = None) -> None:
        if queens:
            self.queens = queens
        else:
            self.queens =  8 * [-1]


    def get(self, i: int) -> int:
        return self.queens[i]


    def set(self, i: int, j: int) -> None:
        self.queens[i] = j


    def is_solved(self) -> bool:
        if -1 in self.queens:
            print("Not all 8 queens set.")
            return False
        
        for i, pos1 in enumerate(self.queens[:-1]):
            for k, pos2 in enumerate(self.queens[i+1:]):
                if pos2 == pos1:
                    return False
                if pos2 == pos1 + (k + 1):
                    return False
                if pos2 == pos1 - (k + 1):
                    return False
        return True


    def print_board(self) -> None:
        for i in self.queens:
            print("| " * i + "|X" + "| " * (7-i) + "|")





def main():

    board1 = EQ()

    board1.set(0, 2)

    board1.set(1, 4)

    board1.set(2, 7)

    board1.set(3, 1)

    board1.set(4, 0)

    board1.set(5, 3)

    board1.set(6, 6)

    board1.set(7, 5)
    board1.print_board()
    print("Is board1 a correct eight queen placement?",

        board1.is_solved())

 

    board2 = EQ([0, 4, 7, 5, 2, 6, 1, 3])

    if board2.is_solved():

        print("Eight queens are placed correctly in board2")

        board2.print_board()

    else:

        print("Eight queens are placed incorrectly in board2")


if __name__ == "__main__":
    main()