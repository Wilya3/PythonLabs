from ThirdLabAuthorTable import AuthorTable
from ThirdLabMenuTable import MenuTable
from ThirdLabContentTable import ContentTable


def loadData(listOfTables):
    for table in listOfTables:
        try:
            print("Введите название файла с таблицей " + table.tableName + " (Без расширения)")
            fileName = input() + ".csv"
            table.load(fileName)
        except KeyError:
            print("Ошибка. Значение ключа повторяется!")
            exit()
        except Exception:
            print("Открыть таблицу " + table.tableName + " не удалось. Создается новый файл...")
            table.createFile()


def chooseTableForAction():
    print("С какой таблицей производится действие? (Menu/Content/Author)")
    requiredTableName = input().capitalize()
    for table in listOfTables:
        if table.tableName == requiredTableName:
            return table
    raise FileNotFoundError


def printAll(tables):
    for table in tables:
        print("\n" + table.tableName)
        table.printTable()


def saveAll(tables):
    for table in tables:
        table.save()


if __name__ == "__main__":
    listOfTables = []
    contentTable = ContentTable("Content")
    menuTable = MenuTable("Menu", contentTable)
    authorTable = AuthorTable("Author", contentTable)
    listOfTables.append(contentTable)
    listOfTables.append(menuTable)
    listOfTables.append(authorTable)
    loadData(listOfTables)
    
    print("Инициализация закончена. Работа с таблицами разрешена")
    while True:
        printAll(listOfTables)
        print("Какое действие необходимо? (add/change/delete/exit)")
        action = input().lower()
        if action != "add" and action != "change" and action != "delete" and action != "exit":
            print("Неверная команда! Повторите ввод")
            continue
        if action == "exit":
            break
        try:
            table = chooseTableForAction()
            if action == "add":
                table.add()
            if action == "change":
                table.change()
            if action == "delete":
                table.delete()
            saveAll(listOfTables)
        except FileNotFoundError:
            print("Ошибка! Таблица с таким именем не найдена. Действие отменяется...")
            continue
        except KeyError:
            print("Ошибка ввода ID таблицы! Действие отменяется...")
            continue
        except IndexError:
            print("Значение столбца недопустимо! Действие отменяется...")
            continue






    print("Название контента" + (" " * 18) + "Название меню" + (" " * 22) + "Ник автора" + (" " * 25) + "Аннотация")
    for key in contentTable.dictionary:
        print(str(contentTable.dictionary[key][0]) +
              (" " * (35 - len(contentTable.dictionary[key][0]))) +
              str(menuTable.dictionary[int(contentTable.dictionary[key][4])][0]) +
              (" " * (35 - len(menuTable.dictionary[int(contentTable.dictionary[key][4])][0]))) +
              str(authorTable.dictionary[int(contentTable.dictionary[key][3])][0]) +
              (" " * (35 - len(authorTable.dictionary[int(contentTable.dictionary[key][3])][0]))) +
              str(contentTable.dictionary[key][1]))


        # chooseAddTable()
        # elif action == "change":
        #     print("В какой таблице происходит изменение данных? (Menu/Content/Author)")
        #     chooseChangeTable()
        # elif action == "delete":
        #     print("Из какой таблицы удаляется запись? (Menu/Content/Author)")
        #     chooseDeleteTable()
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
