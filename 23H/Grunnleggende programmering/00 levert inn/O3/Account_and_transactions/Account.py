from Transaction import Transaction


class Account:
    def __init__(self, customer_id: int, account_number: int, balance: int, interest: int) -> None:
        self.__customer_id = customer_id
        self.__account_number = account_number
        self.__balance = balance
        self.__interest = interest
        self.__transactions = []
    

    def get_balance(self) -> int:
        return self.__balance
    

    def deposit(self, amount: int) -> int:
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(Transaction(amount))
        else:
            print("Deposit Amount is too low.")
        return self.__balance
    

    def withdraw(self, amount: int) -> int:
        if amount <= 0:
            print("Withdraw amount is too low.")
            return self.__balance
        
        if self.__balance - amount >= 0:
            self.__balance -= amount
            self.__transactions.append(Transaction(-amount))
            return self.__balance
        else:
            print("You don't have enough money.")

        


    def show_transactions(self) -> None:
        for transaction in self.__transactions:
            print(f"Transaction time: {transaction.get_time()}, amount: {transaction.get_amount()}")


    def __str__(self) -> str:
         return (f"Customer ID: {self.__customer_id}\n"
                 f"Account number: {self.__account_number}\n"
                 f"Balance: {self.__balance}\n"
                 f"Interest: {self.__interest}\n")



