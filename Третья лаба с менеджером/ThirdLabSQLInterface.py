# TODO: Сравнить сигнатуры с менеджером, когда доделаю его


class SQLInterface:
    """
    Interface for classes which works with DB.
    It works with databases using SQL.\n
    # TODO: Изменить конструктор для наследования
    It HAS TO make cursor of external library
    for DBMS while creating object.
    """

    def __init__(self, name, user, password, host):
        self.cursor = None

    def disconnectFromDB(self):
        """
        ABSTRACT METHOD. Should disconnect from DB
        using cursor from external library.
        :return:
        """
        pass

    def createTable(self, tableName, listOfColumnNames, listOfColumnTypes, listOfColumnNamesPK):
        """
        ABSTRACT METHOD.
        # TODO: Пересмотреть, куда засунуть NOT NULL и DEFAULT
        It has to only create a table and set a PRIMARY KEY [NOT NULL, DEFAULT].\n
        Example: ListOfColumnTypes: ["SERIAL", "INTEGER DEFAULT 0 NOT NULL"]\n
        Others constraints (CHECK, UNIQUE) should be added with "addConstraint()"\n
        :param String tableName:\n
        :param list listOfColumnNames:\n
        :param list listOfColumnTypes:\n
        :param list listOfColumnNamesPK:\n
        """
        pass

    def dropTable(self, tableName):
        """
        Deletes a table\n
        :param String tableName:\n
        """
        pass

    def addColumn(self, tableName, columnName, columnType):
        """
        Adds a new column to the table\n
        :param String tableName:\n
        :param String columnName: \n
        :param String columnType: \n
        """
        pass

    def dropColumn(self, tableName, columnName):
        """
        Drop a column from the table\n
        :param String tableName:\n
        :param String columnName: \n
        """
        pass

    def addConstraintCheck(self, tableName, columnName):
        """
        Add CHECK constraint to the table.\n
        :param String tableName:\n
        :param String columnName: \n
        """
        pass

    def addConstraintUnique(self, tableName, columnName):
        """
        Add UNIQUE constraint to the table.\n
        :param String tableName:\n
        :param String columnName: \n
        """
        pass

    def dropConstraint(self, constraintName):
        """
        Delete constraint by its name.
        :param String constraintName: \n
        """
        pass

    def addValue(self):
        """
        :return:
        """
        pass

    def changeValue(self):
        """
        :return:
        """
        pass

    def deleteValue(self):
        """
        :return:
        """
        pass

    def addValuesIntoTableFromCSV(self):
        pass

    def getValuesFromTableToCSV(self):
        pass



    # def connectToDB(self, name, user, password, host):
    #     """
    #     :param name:
    #     :param user:
    #     :param password:
    #     :param host:
    #     :return connector:
    #     """
    #     return None

    # def createDB(self, name):
    #     # query = "CREATE DATABASE " + str(name)
    #     pass