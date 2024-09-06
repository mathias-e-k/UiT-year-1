class Calculator:
    def __init__(self) -> None:
        self.__log = []

    def calculate(self, operand1: float, operand2: float, operator: str):
        if operator not in ("+", "-", "*", "/"):
            self.__log.append("Invalid operator")
            return 0.0
        try:
            result = eval(f"{operand1} {operator} {operand2}")
        except Exception as e:
            self.__log.append(str(e))
            return 0.0
        self.__log.append(f"{operand1} {operator} {operand2} = {result}")
        return result

    def get_log(self) -> list:
        return self.__log

    def get_last_logged(self) -> str:
        return self.__log[-1]

    def clear_log(self) -> None:
        self.__log.clear()





if __name__ == "__main__":
    calculator = Calculator()
    print(calculator.calculate(1,2,'+'))
    print(calculator.calculate(2,2,'*'))
    print(calculator.calculate(16,2,'/'))
    print(calculator.get_log())
    print(calculator.get_last_logged())
    calculator.clear_log()
    print(calculator.calculate(2,6,'*'))
    print(calculator.calculate(16,6,'/'))
    print(calculator.get_log())