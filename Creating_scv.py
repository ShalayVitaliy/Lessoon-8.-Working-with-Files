def creating():
    file = 'Phonebook.scv'
    with open(file, 'w', encoding='utf-8') as data:
        data.write(f"Фамилия; Имя; Номер телефона; Пояснение \n")