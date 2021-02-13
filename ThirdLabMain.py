import psycopg2
import pandas as pd
from ThirdLabTableSQL import Table
from ThirdLabUI import UIFactory


# TODO: SELECT по лабе №1
# TODO: SELECT по лабе №2
# TODO: Узнать насчет ввода id
# TODO: Слияние, а не удаление

def askTable(listOfTables):
    """
    Find Table object in list and return it.
    :param listOfTables:
    :return Table table:
    """
    print(UI.table())
    requiredName = input().capitalize()
    for table in listOfTables:
        if table.name == requiredName:
            return table
    raise FileNotFoundError  # TODO: Разобраться с ошибками


def askFile(table):
    print(UI.file() + table.name)
    fileName = input() + ".csv"
    return fileName


def printAll(listOfTables):
    for table in listOfTables:
        print("\n" + table.name)
        table.printTable()


def listToPandas(listOfColumns, listOfValues):
    dataFrame = pd.DataFrame()
    columnCounter = 0
    for i in range(len(listOfColumns)):
        columnOfValues = []
        for j in range(len(listOfValues)):
            columnOfValues.append(listOfValues[j][i])
        dataFrame.insert(columnCounter, listOfColumns[i], columnOfValues)
        columnCounter += 1
    return dataFrame


def firstTask(cursor):
    """
    First task from laboratory. Select this:
    Для каждого контента:
    «Название контента»,
    «название меню», «ник
    автора», «аннотация».
    """
    cursor.execute("SELECT content.title, menu.title, author.nick, content.annotation"
                   "\nFROM content"
                   "\nJOIN menu ON (content.id_menu = menu.id)"
                   "\nJOIN author ON (content.id_author = author.id);")
    listOfValues = []
    for row in cursor:
        listOfValues.append(row)
    df = listToPandas(["Название контента", "Название меню", "Ник автора", "Аннотация"], listOfValues)
    print(df)

def secondTask(cursor):
    """

    :param cursor:
    :return:
    """


if __name__ == "__main__":
    connection = psycopg2.connect(dbname='PythonLabs', user='postgres',
                                  password='python', host='localhost')
    connection.autocommit = True
    cursor = connection.cursor()

    tables = [
        Table("Menu", cursor, ["id", "title"]),
        Table("Author", cursor, ["id", "nick", "password", "email"]),
        Table("Content", cursor, ["id", "title", "annotation", "content", "id_author", "id_menu"])
    ]

    Factory = UIFactory()
    UI = Factory.createUI("russian")  # TODO: Должна быть фабрика в идеале
    # TODO: Сделать словарь
    # actions = ["load", "save", "add", "change", "delete", "exit"]

    print(UI.initialization())

    while True:
        print(UI.action() + " (print/first/second/load/save/add/change/delete/exit)")
        action = input().lower()
        if action != "add" and \
                action != "change" and \
                action != "delete" and \
                action != "exit" and \
                action != "load" and \
                action != "first" and \
                action != "second" and \
                action != "print" and \
                action != "save":
            print(UI.wrongCommand())
            continue
        if action == "exit":
            break
        try:
            if action == "print":
                printAll(tables)
                continue

            if action == "first":
                firstTask(cursor)
                continue

            if action == "second":
                continue

            table = askTable(tables)

            if action == "add":
                table.printTable()
                print(UI.values())
                print(table.columns)
                values = input().split(" ")  # Попробовать сломать
                table.add(values)

            if action == "change":
                print(UI.changeWarning() + UI.column())
                column = input()
                print(UI.changeCondition())
                conditionWhere = input()
                print(UI.newValue())
                newValue = input()
                table.change(column, newValue, conditionWhere)

            if action == "delete":
                print(UI.deleteWarning() + UI.deleteCondition())
                condition = input()
                table.delete(condition)

            if action == "save":
                fileName = askFile(table)
                table.save(fileName)

            if action == "load":
                print(UI.loadWarning() + " (y/n)")
                if input() == "y":
                    fileName = askFile(table)
                    table.loadData(fileName)
                else:
                    print(UI.cancel())
                    continue

        # TODO: Разобраться с исключениями
        except FileNotFoundError:
            print("Ошибка! Таблица с таким именем не найдена. Действие отменяется...")
            continue
        # except ValueError: TODO: loadToTemp Error найти
        #     print("Ошибка загрузки файла!")
        except UserWarning:
            print("Ошибка добавления данных в базу данных!"
                  "\nВозможные проблемы:"
                  "\nДанные повреждены или не соответствуют таблице"
                  "\nПовторяются ключи")
        except KeyError:
            print("Ошибка ввода ID таблицы! Действие отменяется...")
            continue
        except IndexError:
            print("Значение столбца недопустимо! Действие отменяется...")
            continue
        finally:
            print(UI.pressAnyButton())
            input()

    cursor.close()
    connection.close()
