from ThirdLabInterfaceCSV import TableCVS


class ContentTable(TableCVS):
    """
    Таблица представлена в виде словаря, где...\n
    Ключ словаря - первый элемент загруженного массива;\n
    Значение словаря - массив из оставшихся элементов загруженного массива \n
    {key : values[]} \n
    0, abc, 88005553535 -> {0 : [abc, 88005553535]}\n
    key - определяет строку.\n\n
    id - [key]
    Название [0]
    Аннотация [1]
    Содержимое [2]
    ID_Автора - ключ таблицы Author [3]
    ID_Меню - ключ таблицы Menu [4]
    """

    def __init__(self, tableName):
        super(ContentTable, self).__init__(tableName, 5)

    def add(self):
        key = self.askKeyForAction()
        if key in self.dictionary:
            print("Ошибка. Запись с таким ключем уже существует")
            raise KeyError
        print("Введите название:")
        listOfValues = [input()]
        print("Введите аннотацию:")
        listOfValues.append(input())
        print("Введите содержимое:")
        listOfValues.append(input())
        print("Введите ID_автора:")
        listOfValues.append(input())
        print("Введите ID_меню:")
        listOfValues.append(input())
        self.dictionary[key] = listOfValues
        print("Запись добавлена.")

    def delete(self):
        key = self.askKeyForAction()
        if not (key in self.dictionary):
            print("Ошибка. Запись с таким ключем не существует")
            raise KeyError
        self.dictionary.pop(key)

    def deleteByParentsID(self, parentsID, parentsIDColumn):
        copyOfDictionary = self.dictionary.copy()
        for i in self.dictionary:
            if self.dictionary[i][parentsIDColumn] == str(parentsID):
                copyOfDictionary.pop(i)
        self.dictionary = copyOfDictionary.copy

    def printTable(self):
        print("ID" + " " * 18, end='')
        print("Название [0]" + " " * 8, end='')
        print("Аннотация [1]" + " " * 7, end='')
        print("Содержимое [2]" + " " * 6, end='')
        print("ID_Автора [3]" + " " * 7, end='')
        print("ID_Меню [4]")
        for key in self.dictionary:
            print(str(key) + " " * (20-len(str(key))), end='')
            for column in self.dictionary[key]:
                print(str(column) + " " * (20-len(column)), end='')
            print()
