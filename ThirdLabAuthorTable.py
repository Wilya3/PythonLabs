from ThirdLabInterfaceCSV import TableCSV


class AuthorTable(TableCSV):
    """
    Таблица представлена в виде словаря, где...\n
    Ключ словаря - первый элемент загруженного массива;\n
    Значение словаря - массив из оставшихся элементов загруженного массива \n
    {key : values[]} \n
    0, abc, 88005553535 -> {0 : [abc, 88005553535]}\n
    key - индекс строки.\n\n
    id[key] - 5 столбец таблицы Content
    Ник[0]
    Пароль[1]
    Почта[2]
    """

    def __init__(self, tableName, daughters):
        super(AuthorTable, self).__init__(tableName, 3)
        self.daughterTables = daughters

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
        print("ID" + " " * 13, end='')
        print("Ник [0]" + " " * 8, end='')
        print("Пароль [1]" + " " * 5, end='')
        print("Почта [2]")
        for key in self.dictionary:
            print(str(key) + " " * (15-len(str(key))), end='')
            for column in self.dictionary[key]:
                print(str(column) + " " * (15-len(column)), end='')
            print()

    def printNumberOfContent(self):
        for authorID in self.dictionary:
            counter = 0
            for key in self.daughterTables.dictionary:
                if self.daughterTables.dictionary[key][3] == str(authorID):
                    counter += 1
            print("Количество контента автора " + self.dictionary[authorID][0] + ": " + str(counter))