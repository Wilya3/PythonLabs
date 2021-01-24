from ThirdLabInterfaceCSV import TableCVS


class ContentTable(TableCVS):
    """
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
        copyOfDictionary = self.dictionary
        for i in self.dictionary:
            if self.dictionary[i][parentsIDColumn] == parentsID:
                copyOfDictionary.pop(i)
        self.dictionary = copyOfDictionary

    def printTable(self):
        print("ID" + " " * 10, end='')
        print("Название [0]" + " " * 10, end='')
        print("Аннотация [1]" + " " * 10, end='')
        print("Содержимое [2]" + " " * 10, end='')
        print("ID_Автора [3]" + " " * 10, end='')
        print("ID_Меню [4]")
        for key in self.dictionary:
            print(str(key) + " " * 10, end='')
            for column in self.dictionary[key]:
                print(str(column) + " " * 10, end='')
            print()