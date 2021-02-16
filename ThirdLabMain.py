import psycopg2
from ThirdLabTableSQL import *
from ThirdLabUI import UIFactory


def askTable(listOfTables):
    """
    Find Table object in list and return it.
    :raise FileNotFoundError:
    :param listOfTables:
    :return Table table:
    """
    print(UI.table())
    requiredName = input().capitalize()
    for table in listOfTables:
        if table.name == requiredName:
            return table
    raise FileNotFoundError


def askFile(table):
    print(UI.file() + table.name)
    fileName = input() + ".csv"
    return fileName


def printAll(listOfTables):
    for table in listOfTables:
        print("\n" + table.name)
        table.printTable()


def firstTask(cursor):
    """
    First task from laboratory. Select this:
    Для каждого контента:
    «Название контента»,
    «название меню», «ник
    автора», «аннотация».
    :param cursor:
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
    First task from laboratory. Select this:
    Для каждого пользователя:
    количество контента,
    которое он добавил.
    :param cursor:
    """
    cursor.execute("SELECT author.nick, COUNT(*) "
                   "FROM author JOIN content ON (author.id = content.id_author)"
                   "GROUP BY author.nick;")
    listOfValues = []
    for row in cursor:
        listOfValues.append(row)
    df = listToPandas(["Ник автора", "Количество контента"], listOfValues)
    print(df)


if __name__ == "__main__":
    Factory = UIFactory()
    UI = Factory.createUI("russian")

    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(dbname='PythonLabs', user='postgres',
                                      password='python', host='localhost')
        connection.autocommit = True
        cursor = connection.cursor()
    except:
        print(UI.connectionError())
        exit()

    tables = [
        Table("Menu", cursor, ["id", "title"]),
        Table("Author", cursor, ["id", "nick", "password", "email"]),
        Table("Content", cursor, ["id", "title", "annotation", "content", "id_author", "id_menu"])
    ]

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
                secondTask(cursor)
                continue

            table = askTable(tables)

            if action == "add":
                table.printTable()
                print(UI.values())
                print(table.columns)
                values = []
                for i in range(len(table.columns)):
                    print(table.columns[i])
                    values.append(input())
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

        except FileNotFoundError:
            print(UI.fileNotFoundError())
            continue
        except QueryError:
            print(UI.queryError())
            continue
        except BadFileError:
            print(UI.badFileError())
            print(UI.cancel())
            continue

    cursor.close()
    connection.close()
