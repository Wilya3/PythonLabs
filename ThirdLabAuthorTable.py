from ThirdLabInterfaceCSV import TableCVS


class AuthorTable(TableCVS):
    """
    id - 5 столбец таблицы Content [key]
    Ник [0]
    Пароль [1]
    Почта [2]
    """

    def __init__(self, tableName, daughters):
        super(AuthorTable, self).__init__(tableName, 3)
        self.daughterTables = [daughters]

    def add(self):
        key = self.askKeyForAction()
        if key in self.dictionary:
            print("Ошибка. Запись с таким ключем уже существует")
            raise KeyError
        print("Введите ник:")
        listOfValues = [input()]
        print("Введите пароль:")
        listOfValues.append(input())
        print("Введите почту:")
        listOfValues.append(input())
        self.dictionary[key] = listOfValues
        print("Запись добавлена.")

    def delete(self):
        key = self.askKeyForAction()
        if not (key in self.dictionary):
            print("Ошибка. Запись с таким ключем не существует")
            raise KeyError
        self.dictionary.pop(key)
        # ГОВНОКОД. Просим дочернюю таблицу (0) удалить все значения,
        # у которых в указанном (связанном) столбце (3) совпадает
        # значение с удаляемым ключом записи нашей таблицы (key)
        self.daughterTables[0].deleteByParentsID(key, 3)

    def printTable(self):
        print("ID" + " " * 10, end='')
        print("Ник [0]" + " " * 10, end='')
        print("Пароль [1]" + " " * 10, end='')
        print("Почта [2]")
        for key in self.dictionary:
            print(str(key) + " " * 10, end='')
            for column in self.dictionary[key]:
                print(str(column) + " " * 10, end='')
            print()