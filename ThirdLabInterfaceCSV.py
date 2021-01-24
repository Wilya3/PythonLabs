import csv, abc


class TableCVS:
    """
    Таблица представлена в виде словаря, где...\n
    Ключ словаря - первый элемент загруженного массива;\n
    Значение словаря - массив из оставшихся элементов загруженного массива \n

    Абстрактные методы add, change, delete \n
    key - определяет строку.
    """

    def __init__(self, tableName):
        self.tableName = tableName
        self.dictionary = {}
        self.filePath = ""

    def load(self, filePath):
        self.filePath = filePath
        with open(self.filePath, "r") as f_obj:
            reader = csv.reader(f_obj)
            for row in reader:
                if row[0] in self.dictionary:  # Если ключ уже есть, кинуть ошибку
                    raise IndexError
                # TODO: Проверить, удаляется ли первое значение списка, после занесения в ключ
                self.dictionary[row.pop(0)] = row

    def createFile(self):
        try:
            with open(self.filePath, "w+"):
                print("Новый файл создан")
        except Exception:
            print("Ошибка создания файла")

    def save(self):
        with open(self.filePath, "w") as f_obf:
            writer = csv.writer(f_obf)
            for key in self.dictionary:
                listOfRow = self.getListByKey(key)
                writer.writerow(listOfRow)

    def add(self):
        """
        Абстрактный метод добавления значения в таблицу! Необходимо перепоределять!\n
        При неправильном key таблицы кидает IndexError\n
        (Переопределять необходимо из-за разного количества столбцов)\n
        """

    def delete(self):
        """
        Абстрактный метод удаления значения из таблицы! Необходимо перепоределять!\n
        При неправильном key таблицы кидает IndexError\n
        (Переопределять необходимо из-за связанности таблиц)\n
        """

    def change(self):  # TODO: Проверить, можно ли реализовать в родительском
        """
        Абстрактный метод изменения данных! Необходимо перепоределять!\n
        При неправильном key таблицы или номере столбца кидает IndexError\n
        (Переопределять необходимо из-за разного количества столбцов)\n
        """
        key = self.askKeyForAction()  # Выбираем строку
        print("Введите номер столбца для изменения")
        try:
            i = int(input())  # Выбираем столбец
            print("Введите новое значение")
            self.dictionary[key][i] = input()
        except Exception:
            raise IndexError


    def getListByKey(self, key):
        """
        Получает номер строки таблицы (key) и преобразует
        данную пару словаря в массив для сохранения. Полученный
        одномерный массив содержит и значение словаря и его ключ.
        :param key:
        :return list:
        """
        listOfRow = [key]
        for column in self.dictionary[key]:
            listOfRow.append(column)
        return listOfRow

    def askKeyForAction(self):
        """
        Получает, проверяет и возвращает ключ.\n
        При ошибке кидает IndexError\n
        :return int key:\n
        """
        print("Введите ID(ключ) записи в виде целого числа")
        try:
            id = int(input())
        except Exception:
            print("Введено не целое число!")
            raise IndexError
        return id
