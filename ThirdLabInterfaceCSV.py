import csv


class TableCVS:
    """
    Таблица представлена в набора словарей, где...
    Ключ словаря - первый элемент полученного массива;\n
    Значение словаря - оставшиеся элементы полученного массива \n

    Для лабораторной:\n
    Меню:\n
    первый элемент - id,\n
    второй элемент - Название\n\n

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
                # TODO: Проверить, удаляется ли первое значение списка, после занесения в ключ
                self.dictionary[row.pop(0)] = row

    def createFile(self):
        try:
            with open(self.filePath, "w+") as f_obj:
                print("Новый файл создан")
        except Exception:
            print("Ошибка создания файла")

    def update(self):  # TODO: update() функцию создать
        pass
