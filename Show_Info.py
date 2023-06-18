def show_info():
    file = 'Phonebook.txt'
    print("\nПП | ФИО | Телефон")
    with open(file, 'r', encoding='utf-8') as data:
        print(data.read())
    print("")
