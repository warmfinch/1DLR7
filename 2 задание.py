password = input("Придумайте пароль: ")
confirm = input("Подтвердите пароль: ")

if password == confirm:
    attempt = input("Введите пароль для входа: ")

    if attempt == password:
        print("Access")
    else:
        print("Denied")
else:
    print("Пароли не совпадают, авторизация невозможна")