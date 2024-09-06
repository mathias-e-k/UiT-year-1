from datetime import datetime


class Transaction:
    def __init__(self, amount: int) -> None:
        now = datetime.now()
        self.__time = now.strftime("%Y-%m-%d %H:%M:%S")
        self.__amount = amount
    

    def get_time(self) -> str:
        return self.__time
    

    def get_amount(self) -> int:
        return self.__amount
    

    def __str__(self) -> str:
        print(f"Time: {self.__time}\nAmount: {self.__amount}")
