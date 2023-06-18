from Show_Info import show_info
from Change_info import change_data
from Delete_Info import delete_data
from Filling_File import filling_txt


def Choice():
    my_choice = 1
    while my_choice != 0:
        print("Выберите одно из действий:")
        print("1 - Вывести инфо на экран")
        print("2 - Произвести экпорт данных")
        print("3 - Произвести изменение данных")
        print("4 - Произвести удаление данных")
        print("0 - Выход из программы")
        action = int(input("Действие: "))
        if action == 1:
            show_info()
        elif action == 2:
            filling_txt()
        elif action == 3:
            change_data()
        elif action == 4:
            delete_data()
        else:
            my_choice = 0

    print("До свидания")



