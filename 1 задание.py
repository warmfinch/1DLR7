direction = input("Введите направление (a, d, w, s): ")

match direction:
    case "a":
        print("Иду влево")
    case "d":
        print("Иду вправо")
    case "w":
        print("Иду прямо")
    case "s":
        print("Иду назад")
    case _:
        print("Неправильное направление")