import csv
from MenuInterface import MenuInterface


def chooseAddTable():
    table = input().capitalize()
    if table == "Menu":
        menuInterface.add()
    elif table == "Content":
        ContentInterface.add()
    elif table == "Author":
        AuthorInterface.add()
    else:
        print("Неверный ввод! Отмена действия.")


def chooseChangeTable():
    table = input().capitalize()
    if table == "Menu":
        menuInterface.change()
    elif table == "Content":
        ContentInterface.change()
    elif table == "Author":
        AuthorInterface.change()
    else:
        print("Неверный ввод! Отмена действия.")


def chooseDeleteTable():
    table = input().capitalize()
    if table == "Menu":
        menuInterface.delete()
    elif table == "Content":
        ContentInterface.delete()
    elif table == "Author":
        AuthorInterface.delete()
    else:
        print("Неверный ввод! Отмена действия.")


if __name__ == "__main__":
    menuInterface = MenuInterface()
    contentInterface = ContentInterface()
    authorInterface = AuthorInterface()


    # TODO: Засунуть ввод названия файла с таблицей в соответствующую функцию класса
    try:
        menuInterface.load()
    except IOError:
        menuInterface.createFile()

    # print("Введите название файла с таблицей Контент")
    # contentFileName = input() + ".csv"
    try:
        ContentInterface.load()
    except IOError:
        ContentInterface.createFile()

    # print("Введите название файла с таблицей Автор")
    # authorFileName = input() + ".csv"
    try:
        AuthorInterface.load()
    except IOError:
        AuthorInterface.createFile()


    while True:
        print("Какое действие необходимо? (add/change/delete)")
        action = input().lower()
        if action == "add":
            print("В какую таблицу добавляется запись? (Menu/Content/Author)")
            chooseAddTable()
        elif action == "change":
            print("В какой таблице происходит изменение данных? (Menu/Content/Author)")
            chooseChangeTable()
        elif action == "delete":
            print("Из какой таблицы удаляется запись? (Menu/Content/Author)")
            chooseDeleteTable()
