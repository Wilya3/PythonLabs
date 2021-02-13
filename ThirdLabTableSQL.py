import csv


def addQuotesToList(list):
    # Числа он самостоятельно к CHARACTER преобразовывает, а любые буквы без одинарных
    # кавычек считает за название столбца.
    """
    Without quotes DB thinks: "trings are columns. I dont have so column"
    :param list:
    :return:
    """
    for i in range(len(list)):
        if not list[i].isdigit():
            list[i] = "'" + list[i] + "'"
    return list

# TODO: Разобраться с try-except
class Table:
    def __init__(self, tableName, cursor, columns):
        self.name = tableName
        self.cursor = cursor
        self.columns = columns  # пока необязательно
        self.tempValues = []  # Double array. First dimension - rows, second - column.

    def loadData(self, filePath):
        """
        Firstly load data to tempList in memory to check file correctness.
        Then clear table and add data from tempList to DB.
        :raise: ValueError - reading from file problem
        :raise: UserWarning - adding to DB problem
        :param: filePath
        """
        try:
            self.loadToTemp(filePath)
            self.delete()
            self.loadTempToDB()
        except Exception:
            raise UserWarning

    def loadToTemp(self, filePath):
        """
        :raise ValueError:
        :param filePath:
        """
        with open(filePath, "r") as f_obf:
            reader = csv.reader(f_obf)
            self.tempValues = []
            for value in reader:
                if len(value) == len(self.columns):
                    readyList = addQuotesToList(value)
                    self.tempValues.append(readyList)

    def loadTempToDB(self):
        """
        Take data from self.tempValues and add to DB.
        """
        query = ""
        for i in range(len(self.tempValues)):  # add rows
            query += "INSERT INTO " + self.name
            query += " VALUES ("
            for j in range(len(self.tempValues[i])):  # add values
                query += self.tempValues[i][j]
                if j != len(self.tempValues[i]) - 1:
                    query += ", "
            query += ");\n"
        self.cursor.execute(query)

    def clear(self):
        query = "DELETE FROM " + self.name + ";"
        self.cursor.execute(query)

    # def createFile(self):
    #     try:
    #         with open(self.filePath, "w+"):
    #             print("Новый файл создан")
    #     except Exception:
    #         print("Ошибка создания файла")

    def save(self, filePath):
        self.cursor.execute("SELECT * FROM " + self.name + ";")
        with open(filePath, "w+") as f_obf:
            writer = csv.writer(f_obf)
            for row in self.cursor:
                writer.writerow(row)

    def add(self, listOfValues):
        """
        Add new values to DB.
        :param list listOfValues:\n
        """
        try:
            readyList = addQuotesToList(listOfValues)
            query = "INSERT INTO " + self.name
            query += "\nVALUES ("
            for i in range(len(readyList)):
                query += readyList[i]
                if i != len(readyList) - 1:
                    query += ", "
            query += ");"
            self.cursor.execute(query)
        except:
            raise BaseException

    def delete(self, conditionWhere=""):
        """
        Delete values from table with specified conditionWhere
        or all values, if conditionWhere is empty.
        :param String conditionWhere:\n
        """
        try:
            query = "DELETE FROM " + self.name
            if conditionWhere != "":
                    query += "\nWHERE " + conditionWhere
            query += ";"
            self.cursor.execute(query)
        except:
            print("Ошибка удаления.")

    def change(self, column, newValue, conditionWhere=""):
        """
        Change value of specified column . conditionWhere is not necessary.\n
        :param String column:\n
        :param String newValue:\n
        :param String conditionWhere:\n
        """
        query = "UPDATE " + self.name + \
                "\nSET " + column + " = '" + newValue + "'"
        if len(conditionWhere) != 0:
            query += "\nWHERE " + conditionWhere
        query += ";"
        self.cursor.execute(query)

    def printTable(self):
        """
        Print all strings from table
        """
        query = "SELECT * FROM " + self.name + ";"
        self.cursor.execute(query)
        for row in self.cursor:
            print(row)
