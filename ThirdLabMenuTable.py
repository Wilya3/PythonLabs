from ThirdLabInterfaceCSV import TableCSV


class MenuTable(TableCSV):
    """
    Таблица представлена в виде словаря, где...\n
    Ключ словаря - первый элемент загруженного массива;\n
    Значение словаря - массив из оставшихся элементов загруженного массива \n
    {key : values[]} \n
    0, abc, 88005553535 -> {0 : [abc, 88005553535]}\n
    key - индекс строки.\n\n
    id[key] - 6 столбец таблицы Content
    Название[0]
    """
    def __init__(self, tableName, daughters):
        super(MenuTable, self).__init__(tableName, 1)
        self.daughterTables = daughters

    def add(self):
        key = self.askKeyForAction()
        if key in self.dictionary:
            print("Ошибка. Запись с таким ключем уже существует")
            raise KeyError
        print("Введите название:")
        self.dictionary[key] = [input()]
        print("Запись добавлена.")

    def delete(self):
        key = self.askKeyForAction()
        if not (key in self.dictionary):
            print("Ошибка. Запись с таким ключем не существует")
            raise KeyError
        self.dictionary.pop(key)
        # ГОВНОКОД. Просим дочернюю таблицу (0) удалить все значения,
        # у которых в указанном (связанном) столбце (4) совпадает
        # значение с удаляемым ключом записи нашей таблицы (key)
        self.daughterTables[0].deleteByParentsID(key, 4)

    def printTable(self):
        print("ID" + " " * 8 + "Название [0]")
        for key in self.dictionary:
            print(str(key) + (" " * (10-len(str(key)))), end='')
            for column in self.dictionary[key]:
                print(str(column) + " " * (10-len(column)), end='')
            print()
