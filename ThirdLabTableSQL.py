import csv


def addQuotesToList(list):
    # Числа он самостоятельно к CHARACTER преобразовывает, а любые буквы без одинарных
    # кавычке считает за название столбца.
    """
    Without quotes DB thinks: "trings are columns. I dont have so column"
    :param list:
    :return:
    """
    for i in range(len(list)):
        if not list[i].isdigit():
            list[i] = "'" + list[i] + "'"
    return list


class Table:
    def __init__(self, tableName, cursor, columns):
        self.name = tableName
        self.cursor = cursor
        self.columns = columns  # пока необязательно
        self.tempValues = []  # Double array. First dimension - rows, second - column.

    def loadToTemp(self, filePath):
        """
        :raise ValueError:
        :param filePath:
        """
        try:
            with open(filePath, "r") as f_obf:
                reader = csv.reader(f_obf)  # TODO: Проверка на соответствие столбцов
                self.tempValues = []
                for value in reader:
                    if len(value) == len(self.columns):
                        readyList = addQuotesToList(value)
                        self.tempValues.append(readyList)
                print(self.tempValues)  # TODO: Убрать
        except:
            raise ValueError

    def loadToDB(self):
        """
        Take data from self.tempValues and add to DB.
        """
        query = ""
        for i in range(len(self.tempValues)):  # add rows
            query += "INSERT INTO " + self.name
            query += " VALUES ("
            for j in range(len(self.tempValues[i])):  # add values
                query += self.tempValues[i][j]
                if j != len(self.tempValues[i]) - 1:
                    query += ", "
            query += ");\n"
        self.cursor.execute(query)

    def clear(self):
        query = "DELETE FROM " + self.name + ";"
        self.cursor.execute(query)

    def createFile(self):
        try:
            with open(self.filePath, "w+"):
                print("Новый файл создан")
        except Exception:
            print("Ошибка создания файла")

    def save(self):
        with open(self.filePath, "w+") as f_obf:
            writer = csv.writer(f_obf)
            for key in self.dictionary:
                listOfRow = self.getListByKey(key)
                writer.writerow(listOfRow)

    def add(self):
        """
        Абстрактный метод добавления значения в таблицу! Необходимо перепоределять!\n
        При неправильном key таблицы кидает KeyError\n
        (Переопределять необходимо из-за разного количества столбцов)\n
        """

    def delete(self):
        """
        Абстрактный метод удаления значения из таблицы! Необходимо перепоределять!\n
        При неправильном key таблицы кидает KeyError\n
        (Переопределять необходимо из-за связанности таблиц)\n
        """

    def change(self):
        """
        Изменяет выбранный столбец таблицы. Не изменяет ключи таблиц.
        Не поддерживает связанность с другими таблицами.
        """

    def printTable(self):
        """
        Print all strings from table
        """
        query = "SELECT * FROM " + self.name + ";"
        self.cursor.execute(query)
        for row in self.cursor:
            print(row)

    # def getListByKey(self, key):
    #     """
    #     Необходим для сохранения словаря в файл.\n
    #     Получает номер строки таблицы (key) и преобразует
    #     данную пару словаря в массив для сохранения. Полученный
    #     одномерный массив содержит и значение словаря, и его ключ.
    #     :param key:
    #     :return list:
    #     """
    #     listOfRow = list.copy(self.dictionary[key])
    #     listOfRow.insert(0, key)
    #     return listOfRow
    #
    # def askKeyForAction(self):  # TODO: Вынести в функцию
    #     """
    #     Получает, проверяет и возвращает ключ.\n
    #     При ошибке кидает KeyError\n
    #     :return int key:\n
    #     """
    #     print("Введите ID(ключ) записи в виде целого числа")
    #     try:
    #         key = int(input())
    #     except Exception:
    #         print("Введено не целое число!")
    #         raise KeyError
    #     return key
