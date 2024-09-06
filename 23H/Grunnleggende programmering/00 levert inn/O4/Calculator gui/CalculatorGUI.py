from tkinter import *
from Calculator import Calculator


class CalculatorGUI:
    def __init__(self) -> None:
        self.calculator = Calculator()

        window = Tk()
        window.title("Calculator GUI")

        frame1 = Frame(window)
        frame1.pack()

        label1 = Label(frame1, text="Operand 1")
        self.operand1 = StringVar()
        entry_operand1 = Entry(frame1, textvariable=self.operand1)
        label1.grid(row=1, column=1)
        entry_operand1.grid(row=1, column=2)

        label2 = Label(frame1, text="Operator (+ - * /)")
        self.operator = StringVar()
        entry_operator = Entry(frame1, textvariable=self.operator, width=1)
        label2.grid(row=2, column=1)
        entry_operator.grid(row=2, column=2)

        label3 = Label(frame1, text="Operand 2")
        self.operand2 = StringVar()
        entry_operand2 = Entry(frame1, textvariable=self.operand2)
        label3.grid(row=3, column=1)
        entry_operand2.grid(row=3, column=2)

        label4 = Label(frame1, text="Result")
        self.result = StringVar()
        label_results = Label(frame1, textvariable=self.result)
        label4.grid(row=4, column=1)
        label_results.grid(row=4, column=2)


        frame2 = Frame(window)
        frame2.pack()

        button_calculate = Button(frame2, text="Calculate", command=self.calculate)
        button_clear_log = Button(frame2, text="Clear log", command=self.clear_log)
        button_quit = Button(frame2, text="Quit", command=window.destroy)
        button_calculate.grid(row=1, column=1)
        button_clear_log.grid(row=1, column=2)
        button_quit.grid(row=1, column=3)

        self.log = Text(window, width=30, height=10)
        self.log.pack()
        self.log.insert(1.0, "Log:")

        window.mainloop()

    def calculate(self):
        self.result.set(self.calculator.calculate(self.operand1.get(), self.operand2.get(), self.operator.get()))
        self.log.insert(END, "\n"+self.calculator.get_last_logged())

    def clear_log(self):
        self.calculator.clear_log()
        self.log.delete(2.0, END)




if __name__ == "__main__":
    CalculatorGUI()