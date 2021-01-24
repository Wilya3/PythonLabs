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
        super(ContentTable, self).__init__(tableName)

    def add(self):
        key = self.askKeyForAction()
        if key in self.dictionary:
            print("Ошибка. Запись с таким ключем уже существует")
            raise IndexError
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
            raise IndexError
        self.dictionary.popitem(key)

    def deleteByParentsID(self, parentsID, parentsIDColumn):
        copyOfDictionary = self.dictionary
        for i in self.dictionary:
            if self.dictionary[i][parentsIDColumn] == parentsID:
                copyOfDictionary.popitem(i)
        self.dictionary = copyOfDictionary
