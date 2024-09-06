# Koden er kjørbar og har den funksjonalitet som er etterspurt

def parse_postfix_expression(expression: str) -> int:
    stack = []
    numbers = "0123456789"
    operators = "+-*/"

    for c in expression:
        if c in numbers:
            stack.append(int(c))
        elif c in operators:
            num2 = stack.pop()
            num1 = stack.pop()
            if c == "+":
                result = num1 + num2
            if c == "-":
                result = num1 - num2
            if c == "*":
                result = num1 * num2
            if c == "/":
                result = num1 // num2
            stack.append(result)
        else:
            raise ValueError(f"Unsupported operator: {c}")
    return stack.pop()

if __name__ == "__main__":
    print(parse_postfix_expression("26+2*")) # 16