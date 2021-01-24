from ThirdLabInterfaceCSV import TableCVS


class MenuTable(TableCVS):
    """
    id - 6 столбец таблицы Content [key]
    Название [0]
    """
    def __init__(self, tableName, daughters):
        super(MenuTable, self).__init__(tableName)
        self.daughterTables = daughters

    def add(self):
        key = self.askKeyForAction()
        if key in self.dictionary:
            print("Ошибка. Запись с таким ключем уже существует")
            raise IndexError
        print("Введите название:")
        self.dictionary[key] = input()
        print("Запись добавлена.")

    def delete(self):
        key = self.askKeyForAction()
        if not (key in self.dictionary):
            print("Ошибка. Запись с таким ключем не существует")
            raise IndexError
        self.dictionary.popitem(key)
        # ГОВНОКОД. Просим дочернюю таблицу (0) удалить все значения,
        # у которых в указанном (связанном) столбце (4) совпадает
        # значение с удаляемым ключом записи нашей таблицы (key)
        self.daughterTables[0].deleteByParentsID(key, 4)
