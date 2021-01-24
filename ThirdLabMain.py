from ThirdLabInterfaceCSV import TableCVS
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
    isTableFound = False
    for table in listOfTables:
        if table.tableName == requiredTableName:
            return table
    if not isTableFound:
        raise FileNotFoundError


def printAll(tables):
    for table in tables:
        table.printTable()


if __name__ == "__main__":
    listOfTables = []
    listOfTables.append(ContentTable("Content"))
    listOfTables.append(MenuTable("Menu", [listOfTables[0]]))
    listOfTables.append(AuthorTable("Author", [listOfTables[0]]))
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
            exit()
        try:
            table = chooseTableForAction()
            if action == "add":
                table.add()
            if action == "change":
                table.change()
            if action == "delete":
                table.delete()
            # isTableFound = True
            for table in listOfTables:
                table.save()
        except FileNotFoundError:
            print("Ошибка! Таблица с таким именем не найдена. Действие отменяется...")
            continue
        except KeyError:
            print("Ошибка ввода ID таблицы! Действие отменяется...")
            continue
        except IndexError:
            print("Значение столбца недопустимо! Действие отменяется...")
            continue

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
