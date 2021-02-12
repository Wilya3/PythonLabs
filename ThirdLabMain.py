import psycopg2
from ThirdLabTableSQL import Table


# TODO: Сделать не удаление, а слияние


def askTableForAction(listOfTables):
    print("С какой таблицей производится действие? (Menu/Content/Author)")
    requiredName = input().capitalize()
    for table in listOfTables:
        if table.name == requiredName:
            return table
    raise FileNotFoundError


def printAll(listOfTables):
    for table in listOfTables:
        print("\n" + table.name)
        table.printTable()


def askFile(table):
    print("Введите название файла с таблицей " + table.name + " (Без расширения)")
    fileName = input() + ".csv"
    return fileName


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
    # TODO: Сделать словарь
    # actions = ["load", "save", "add", "change", "delete", "exit"]

    print("Инициализация закончена. Работа с таблицами разрешена")

    while True:
        printAll(tables)
        print("Какое действие необходимо? (load/save/add/change/delete/exit)")
        action = input().lower()
        if action != "add" and \
                action != "change" and \
                action != "delete" and \
                action != "exit" and \
                action != "load" and \
                action != "save":
            print("Неверная команда! Повторите ввод")
            continue
        if action == "exit":
            break
        try:
            table = askTableForAction(tables)
            if action == "add":
                table.add()
            if action == "change":
                table.change()
            if action == "delete":
                table.delete()
            if action == "save":
                fileName = askFile(table)
                table.save(fileName)
            if action == "load":
                print("Вы уверены? Все данные в БД будут перезаписаны данными из файла!"
                      "Дочерние таблицы будут очищены! (y/n)")
                if input() == "y":
                    fileName = askFile(table)
                    table.loadData(fileName)
                else:
                    print("Отмена команды...")
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

    cursor.close()
    connection.close()

    # print("Название контента" + (" " * 18) + "Название меню" + (" " * 22) + "Ник автора" + (" " * 25) + "Аннотация")
    # for key in contentTable.dictionary:
    #     print(str(contentTable.dictionary[key][0]) +
    #           (" " * (35 - len(contentTable.dictionary[key][0]))) +
    #           str(menuTable.dictionary[int(contentTable.dictionary[key][4])][0]) +
    #           (" " * (35 - len(menuTable.dictionary[int(contentTable.dictionary[key][4])][0]))) +
    #           str(authorTable.dictionary[int(contentTable.dictionary[key][3])][0]) +
    #           (" " * (35 - len(authorTable.dictionary[int(contentTable.dictionary[key][3])][0]))) +
    #           str(contentTable.dictionary[key][1]))
    #
    # authorTable.printNumberOfContent()
