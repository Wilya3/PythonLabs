

class SQLQueryManager:
    """
    Interface for automatically creating queries.
    It works with databases using SQL transaction language.\n
    Methods DON'T EXECUTE a SQL query. They only
    create a string of query and return it.\n
    It HAS TO make cursor of external library
    for DBMS while creating object.
    """

    # TODO: Изменить конструктор для наследования
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
        DOESNT EXECUTE A QUERY. Only returns SQL query\n
        It has to only create a table and set a PRIMARY KEY.\n
        Example: ListOfColumnTypes: ["SERIAL", "INTEGER DEFAULT 0 NOT NULL"]\n
        Others constraints (CHECK, UNIQUE) should be added with "addConstraint()"\n
        :param String tableName:\n
        :param list listOfColumnNames:\n
        :param list listOfColumnTypes:\n
        :param list listOfColumnNamesPK:\n
        :return String query:
        """
        if len(listOfColumnNames) != len(listOfColumnTypes):
            raise ValueError("Number of columns not equals number of types")
        # TODO: Исправить проверку! Добавить проверку на типы в дочернем методе
        for PKName in listOfColumnNamesPK:
            if PKName in listOfColumnNames:
                raise ValueError("Primary key column's name is invalid")

        query = "CREATE TABLE " + tableName + "\n(\n"
        for i in range(len(listOfColumnNames)):
            query += listOfColumnNames[i] + listOfColumnTypes[i] + ",\n"

        query += "PRIMARY KEY ("
        for i in range(len(listOfColumnNamesPK)):
            query += listOfColumnNamesPK[i]
            if i != len(listOfColumnNamesPK) - 1:
                query += ", "
        query += ")"
        query += "\n);"
        return query

    def dropTable(self, tableName):
        """
        DOESNT EXECUTE A QUERY. Only returns SQL query\n
        Deletes a table\n
        :param String tableName:\n
        :return String query:
        """
        query = "DROP TABLE " + tableName

    def addColumn(self, tableName, columnName, columnType):
        """
        DOESNT EXECUTE A QUERY. Only returns SQL query\n
        Adds a new column to the table\n
        :param String tableName:\n
        :param String columnName: \n
        :param String columnType: \n
        :return String query:
        """
        query = "ALTER TABLE " + tableName + "\nADD COLUMN " + columnName + " " + columnType
        return query

    def dropColumn(self, tableName, columnName):
        """
        DOESNT EXECUTE A QUERY. Only returns SQL query\n
        Drop a column from the table\n
        :return String query:
        """
        query = "ALTER TABLE " + tableName + "\nDROP COLUMN " + columnName
        return query

    def addConstraintCheck(self, tableName, constraintName, ):
        """
        DOESNT EXECUTE A QUERY. Only returns SQL query\n
        Add CHECK constraint to the table.\n
        :return String query:
        """

    def addConstraintUnique(self, tableName, constraintName, ):
        """
        DOESNT EXECUTE A QUERY. Only returns SQL query\n
        Add UNIQUE constraint to the table.\n
        :return String query:
        """

    def dropConstraint(self):
        """
        :return:
        """

    def addValue(self):
        """
        :return:
        """

    def changeValue(self):
        """
        :return:
        """

    def deleteValue(self):
        """
        :return:
        """




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