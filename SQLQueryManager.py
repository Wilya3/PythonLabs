

class SQLQueryManager:
    """
    Utility class for automatically creating queries.
    It works with databases using SQL transaction language.\n
    Methods DON'T EXECUTE a SQL query. They only
    create a string of query and return it.\n
    """

    def createTable(self, tableName, listOfColumnNames, listOfColumnTypesAnd, listOfColumnNamesPK):
        """
        # TODO: Определить, где вводятся "настройки" столбцов
        DOESNT EXECUTE A QUERY. Only returns SQL query\n
        It has to only create a table and set a PRIMARY KEY [NOT NULL, DEFAULT].\n
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
        # TODO: Переделать место, где присваивается PRIMARY KEY
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
        query = "ALTER TABLE " + tableName + \
                "\nADD COLUMN " + columnName + " " + columnType
        return query

    def dropColumn(self, tableName, columnName):
        """
        DOESNT EXECUTE A QUERY. Only returns SQL query\n
        Drop a column from the table\n
        :param String tableName:\n
        :param String columnName: \n
        :return String query:
        """
        query = "ALTER TABLE " + tableName + \
                "\nDROP COLUMN " + columnName
        return query

    def addConstraintCheck(self, tableName, constraintName, checkCondition):
        """
        DOESNT EXECUTE A QUERY. Only returns SQL query\n
        Add CHECK constraint to the table.\n
        :param String tableName:\n
        :param String constraintName:\n
        :param String checkCondition:\n
        :return String query:
        """
        query = "ALTER TABLE " + tableName + \
                "\nADD CONSTRAINT " + constraintName + " CHECK (" + checkCondition + ");"
        return query

    def addConstraintUnique(self, tableName, columnName, constraintName):
        """
        DOESNT EXECUTE A QUERY. Only returns SQL query\n
        Add UNIQUE constraint to the table.\n
        :param String tableName:\n
        :param String constraintName:\n
        :param String columnName:\n
        :return String query:
        """
        query = "ALTER TABLE " + tableName + \
                "\nADD CONSTRAINT " + constraintName + " UNIQUE (" + columnName + ");"
        return query

    def dropConstraint(self, tableName, constraintName):
        """
        :param String tableName:\n
        :param String constraintName:\n
        :return String query:
        """
        query = "ALTER TABLE " + tableName + \
                "\nDROP CONSTRAINT " + constraintName + ";"
        return query

    def addValue(self, tableName, listOfValues, listOfColumns=[]):
        """
        TODO: Доделать везде комментарии
        If listOfColumns is empty, then all columns to fill necessary.\n
        :param String tableName:\n
        :param list listOfValues:\n
        :param list listOfColumns:\n
        :return String query:
        """
        query = "INSERT INTO " + tableName
        if len(listOfColumns) != 0:
            query += " ("
            for i in range(len(listOfColumns)):
                query += listOfColumns[i]
                if i != len(listOfColumns) - 1:
                    query += ", "
            query += ")"
        query += "\nVALUES ("
        for i in range(len(listOfValues)):
            query += listOfValues[i]
            if i != len(listOfValues) - 1:
                query += ", "
        query += ");"
        return query

    def changeValue(self, tableName, columnName, newValue, conditionWhere=""):
        """
        Change value of specified column. conditionWhere is not necessary.\n
        :param String tableName:\n
        :param String columnName:\n
        :param String newValue:\n
        :param String conditionWhere:\n
        :return String query:
        """
        query = "UPDATE " + tableName + \
                "\nSET " + columnName + " = " + newValue
        if len(conditionWhere) != 0:
            query += "\nWHERE " + conditionWhere
        query += ";"
        return query

    def deleteValue(self, tableName, conditionWhere):
        """
        Delete values from table with specified conditionWhere.\n
        :param String tableName:\n
        :param String conditionWhere:\n
        :return String query:
        """
        query = "DELETE FROM " + tableName + \
                "\nWHERE " + conditionWhere + ";"
        return query

    def getValue(self, tableName, listOfColumns=[], conditionWhere=""):
        """
        Select values of specified columns (all columns, if listOfTables is empty).
         conditionWhere is not necessary also.\n
        :param String tableName:\n
        :param list listOfColumns:\n
        :param String conditionWhere:\n
        :return String query:
        """
        query = "SELECT "
        if len(listOfColumns) == 0:
            query += "*"
        else:
            for i in range(len(listOfColumns)):
                query += listOfColumns[i]
                if i != len(listOfColumns) - 1:
                    query += ", "
        query += "\nFROM " + tableName
        if len(conditionWhere) != 0:
            query += "\nWHERE" + conditionWhere
        query += ";"
        return query





    # SUKAAAAAAAAAAAAAAAA BLYAT NADOELO YZHE
    # def createDB(self, name):
    #     # query = "CREATE DATABASE " + str(name)
    #     pass

    # def getValue(self, listOfTables, listOfColumns=[], conditionWhere="", conditionInnerJoins=[]):
    #     """
          # TODO: Сделать создание SELECT'а с JOIN'ами
    #     :return:
    #     """
    #     query = "SELECT "
    #     if len(listOfColumns) == 0:
    #         query += "* "
    #     else:
    #         for i in range(len(listOfColumns)):
    #             query += listOfColumns[i]
    #             if i != len(listOfColumns) - 1:
    #                 query += ", "
    #     Акщь