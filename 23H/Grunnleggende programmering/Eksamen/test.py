import random as r
fruits = ["banana","apple","orange" ]
numbers = ["one","two","three","four","five"]
for _ in range(5):
    number = r.randint(0,4)
    fruit = r.randint(0,2)
    print(f"You got {numbers[number]} {fruits[fruit]}{'s' if number != 0 else ''}")
    #You got three bananas