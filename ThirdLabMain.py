from ThirdLabInterfaceCSV import TableCVS


# def chooseAddTable():
#     table = input().capitalize()
#     if table == "Menu":
#         menuInterface.add()
#     elif table == "Content":
#         contentInterface.add()
#     elif table == "Author":
#         authorInterface.add()
#     else:
#         print("Неверный ввод! Отмена действия.")
#
#
# def chooseChangeTable():
#     table = input().capitalize()
#     if table == "Menu":
#         menuInterface.change()
#     elif table == "Content":
#         contentInterface.change()
#     elif table == "Author":
#         authorInterface.change()
#     else:
#         print("Неверный ввод! Отмена действия.")
#
#
# def chooseDeleteTable():
#     table = input().capitalize()
#     if table == "Menu":
#         menuInterface.delete()
#     elif table == "Content":
#         contentInterface.delete()
#     elif table == "Author":
#         authorInterface.delete()
#     else:
#         print("Неверный ввод! Отмена действия.")


if __name__ == "__main__":
    listOfTables = []
    listOfTables.append(TableCVS("Menu"))
    listOfTables.append(TableCVS("Content"))
    listOfTables.append(TableCVS("Author"))

    for table in listOfTables:
        try:
            print("Введите название файла с таблицей " + table.tableName + " (Без расширения)")
            fileName = input() + ".csv"
            table.load(fileName)
        except:
            print("Открыть таблицу " + table.tableName + " не удалось. Создается новый файл...")
            table.createFile()

    print("Инициализация закончена. Работа с таблицами разрешена.")
    while True:
        print("Какое действие необходимо? (add/change/delete)")
        action = input().lower()
        if action != "add" and action != "change" and action != "delete":
            print("Неверная команда! Повторите ввод")
            continue

        print("В какую таблицу добавляется запись? (Menu/Content/Author)")
        requiredTableName = input().capitalize()
        isTableFound = False
        for table in listOfTables:
            if table.tableName == requiredTableName:
                if action == "add":
                    table.add()
                if action == "change":
                    table.change()
                if action == "delete":
                    table.delete()
                isTableFound = True
                break
        if not isTableFound:
            print("Ошибка ввода таблицы. Повторите попытку снова")
            continue



        # chooseAddTable()
        # elif action == "change":
        #     print("В какой таблице происходит изменение данных? (Menu/Content/Author)")
        #     chooseChangeTable()
        # elif action == "delete":
        #     print("Из какой таблицы удаляется запись? (Menu/Content/Author)")
        #     chooseDeleteTable()
