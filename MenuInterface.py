import csv

class MenuInterface:
    """
    Таблица представлена в виде двумерного массива,
    где записи хранятся в виде вложенных массивов, где
    первый элемент - id,
    второй элемент - Название
    """

    def __init__(self):
        self.list = []
        self.filePath = ""

    def load(self):
        print("Введите название файла с таблицей Меню (Без расширения)")
        self.filePath = input() + ".csv"

        with open(self.filePath, "r") as f_obj:
            reader = csv.reader(f_obj)
            for row in reader:
                self.list.append(row)

    def createFile(self):
        with open(self.filePath, "w+") as f_obj:
            print("Новый файл создан")
