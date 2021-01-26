import csv


class TableCVS:
    """
    Таблица представлена в виде словаря, где...\n
    Ключ словаря - первый элемент загруженного массива;\n
    Значение словаря - массив из оставшихся элементов загруженного массива \n
    {key : values[]} \n
    0, abc, 88005553535 -> {0 : [abc, 88005553535]}\n
    Абстрактные методы add, delete \n
    key - определяет строку.
    """

    # TODO: Использовать имена

    def __init__(self, tableName, lengthOfValues):
        self.tableName = tableName
        self.dictionary = {}
        self.filePath = ""
        self.lengthOfValues = lengthOfValues

    def load(self, filePath):
        self.filePath = filePath
        with open(self.filePath, "r") as f_obj:
            reader = csv.reader(f_obj)
            for row in reader:
                if len(row) > 0:
                    if row[0] in self.dictionary and len(row) != 0:  # Если ключ уже есть, кинуть ошибку
                        raise KeyError
                    # Массив без ключа (только values) должен быть равен указанной длине
                    if len(row) - 1 != self.lengthOfValues:
                        raise Exception
                    self.dictionary[int(row.pop(0))] = row

    def createFile(self):  # TODO: Не перезаписывать неподходящий файл, а создавать новый файл рядом
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
        Изменяет выбранный столбец данной. Не изменяет ключи таблиц.
        Не поддерживает связанность с другими таблицами.
        """
        key = self.askKeyForAction()  # Выбираем строку
        if not key in self.dictionary:
            raise KeyError
        print("Введите номер столбца для изменения")
        i = int(input())  # Выбираем столбец
        if i < 0 or i >= self.lengthOfValues:
            raise IndexError
        print("Введите новое значение")
        self.dictionary[key][i] = input()

    def printTable(self):
        """
        Выводит словарь.
        (Переопределять необходимо для более удобного представления)
        """
        print(self.dictionary)

    def getListByKey(self, key):
        """
        Необходим для сохранения словаря в файл.\n
        Получает номер строки таблицы (key) и преобразует
        данную пару словаря в массив для сохранения. Полученный
        одномерный массив содержит и значение словаря, и его ключ.
        :param key:
        :return list:
        """
        listOfRow = list.copy(self.dictionary[key])
        listOfRow.insert(0, key)
        return listOfRow

    def askKeyForAction(self):  # TODO: Вынести в функцию
        """
        Получает, проверяет и возвращает ключ.\n
        При ошибке кидает KeyError\n
        :return int key:\n
        """
        print("Введите ID(ключ) записи в виде целого числа")
        try:
            key = int(input())
        except Exception:
            print("Введено не целое число!")
            raise KeyError
        return key
