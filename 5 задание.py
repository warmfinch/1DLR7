import math

num1, sign, num2 = input("Введите число 1, знак и число 2 через пробел: ").split()
num1 = float(num1)
num2 = float(num2)

match sign:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        result = num1 / num2
    case "%":
        result = num1 % num2
    case "//":
        result = num1 // num2
    case "**":
        result = num1 ** num2
    case "%%":
        result = num1 * num2 / 100
    case "/**":
        result = math.sqrt(num1)
    case _:
        result = None

if result is None:
    print("Неизвестный знак")
else:
    print(f"{num1} {sign} {num2} = {result}")