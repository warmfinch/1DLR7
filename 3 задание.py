text = input("Введите текст: ")

word = input("Введите слово: ")

if word in text:
    count = text.count(word)
    print(f'Слово "{word}" есть в тексте, оно встречается {count} раз')
else:
    print(f'Слова "{word}" нет в тексте')