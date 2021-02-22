import csv
import pandas as pd


def addQuotesToList(list):
    # Числа он самостоятельно к CHARACTER преобразовывает, а любые буквы без одинарных
    # кавычек считает за название столбца.
    """
    Without quotes DB thinks: "Strings are columns. I don't have so column"
    :param list:
    :return listWithQuotes:
    """
    for i in range(len(list)):
        if not list[i].isdigit():
            list[i] = "'" + list[i] + "'"
    return list


def listToPandas(listOfColumns, listOfValues):
    pd.set_option('display.max_columns', None)
    dataFrame = pd.DataFrame()
    columnCounter = 0
    for i in range(len(listOfColumns)):
        columnOfValues = []
        for j in range(len(listOfValues)):
            columnOfValues.append(listOfValues[j][i])
        dataFrame.insert(columnCounter, listOfColumns[i], columnOfValues)
        columnCounter += 1
    return dataFrame


class Table:
    def __init__(self, tableName, cursor, columns):
        self.name = tableName
        self.cursor = cursor
        self.columns = columns  # пока необязательно

    def loadData(self, filePath):
        """
        Firstly load data to tempList in memory to check file correctness.
        Then clear table and add data from tempList to DB.
        tempList - Double array. First dimension - rows, second - column.
        :raise: BadFileError - reading from file problem
        :raise: QueryError - adding to DB problem
        :param: filePath
        """
        tempList = self.loadToTemp(filePath)
        self.delete()
        self.loadTempToDB(tempList)

    def loadToTemp(self, filePath):
        """
        Load data to tempList in memory to check file correctness.
        :raise BadFileError:
        :param filePath:
        """
        try:
            with open(filePath, "r") as f_obf:
                reader = csv.reader(f_obf)
                tempList = []
                for value in reader:
                    if len(value) == len(self.columns):
                        readyList = addQuotesToList(value)
                        tempList.append(readyList)
            return tempList
        except:
            raise BadFileError

    def loadTempToDB(self, tempList):
        """
        Take data from self.tempValues and add to DB.
        :raise QueryError:
        """
        try:
            query = ""
            for i in range(len(tempList)):  # add rows
                query += "INSERT INTO " + self.name
                query += " VALUES ("
                for j in range(len(tempList[i])):  # add values
                    query += tempList[i][j]
                    if j != len(tempList[i]) - 1:
                        query += ", "
                query += ");\n"
            self.cursor.execute(query)
        except:
            raise QueryError

    def save(self, filePath):
        """
        Save table to specified file.
        :param String filePath:
        """
        self.cursor.execute("SELECT * FROM " + self.name + ";")
        with open(filePath, "w+") as f_obf:
            writer = csv.writer(f_obf)
            for row in self.cursor:
                writer.writerow(row)

    def add(self, listOfValues):
        """
        Add new values to DB.
        :raise QueryError:
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
            raise QueryError

    def delete(self, conditionWhere=""):
        """
        Delete values from table with specified conditionWhere
        or all values, if conditionWhere is empty.
        :raise QueryError:
        :param String conditionWhere:\n
        """
        try:
            query = "DELETE FROM " + self.name
            if conditionWhere != "":
                query += "\nWHERE " + conditionWhere
            query += ";"
            self.cursor.execute(query)
        except:
            raise QueryError

    def change(self, column, newValue, conditionWhere=""):
        """
        Change value of specified column . conditionWhere is not necessary.\n
        :raise QueryError:
        :param String column:\n
        :param String newValue:\n
        :param String conditionWhere:\n
        """
        try:
            query = "UPDATE " + self.name + \
                    "\nSET " + column + " = '" + newValue + "'"
            if len(conditionWhere) != 0:
                query += "\nWHERE " + conditionWhere
            query += ";"
            self.cursor.execute(query)
        except:
            raise QueryError

    def printTable(self):
        """
        Print all strings from table
        """
        query = "SELECT * FROM " + self.name + ";"
        self.cursor.execute(query)
        listOfValues = []
        for row in self.cursor:
            listOfValues.append(row)
        dataFrame = listToPandas(self.columns, listOfValues)
        if len(dataFrame) != 0:
            print(dataFrame)


class QueryError(Exception):
    pass

class BadFileError(Exception):
    pass
