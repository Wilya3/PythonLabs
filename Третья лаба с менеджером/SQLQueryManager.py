"""
Utility class for automatically creating queries.
It works with databases using SQL transaction language.\n
Methods DON'T EXECUTE a SQL query. They only
create a string of query and return it.\n
"""


def createTable(tableName, listOfColumnNames, listOfColumnTypesAndNullDefault, listOfColumnNamesPK):
    """
    DOESNT EXECUTE A QUERY. Only returns SQL query\n
    It has to only create a table and set names, types [and NOT NULL, DEFAULT]
    of columns. Also set a PRIMARY KEY.\n
    Example: listOfColumnTypes:["SERIAL", "INTEGER DEFAULT 0 NOT NULL"]\n
    Others constraints (CHECK, UNIQUE) should be added with "addConstraint()"\n
    :param String tableName:\n
    :param list listOfColumnNames:\n
    :param list listOfColumnTypesAndNullDefault:\n
    :param list listOfColumnNamesPK:\n
    :return String query:
    """
    if len(listOfColumnNames) != len(listOfColumnTypesAndNullDefault):
        raise ValueError("Number of columns not equals number of types")
    # TODO: Исправить проверку! Добавить проверку на типы в дочернем методе
    for PKName in listOfColumnNamesPK:
        if PKName in listOfColumnNames:
            raise ValueError("Primary key column's name is invalid")

    query = "CREATE TABLE " + tableName + "\n(\n"
    for i in range(len(listOfColumnNames)):
        query += listOfColumnNames[i] + listOfColumnTypesAndNullDefault[i] + ",\n"
    # TODO: Переделать место, где присваивается PRIMARY KEY
    query += "PRIMARY KEY ("
    for i in range(len(listOfColumnNamesPK)):
        query += listOfColumnNamesPK[i]
        if i != len(listOfColumnNamesPK) - 1:
            query += ", "
    query += ")"
    query += "\n);"
    return query


def dropTable(tableName):
    """
    DOESNT EXECUTE A QUERY. Only returns SQL query\n
    Deletes a table\n
    :param String tableName:\n
    :return String query:
    """
    query = "DROP TABLE " + tableName


def addColumn(tableName, columnName, columnType):
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


def dropColumn(tableName, columnName):
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


def addConstraintCheck(tableName, constraintName, checkCondition):
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


def addConstraintUnique(tableName, constraintName, columnName):
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


def dropConstraint(tableName, constraintName):
    """
    DOESNT EXECUTE A QUERY. Only returns SQL query\n
    Delete constraint by its name.
    :param String tableName:\n
    :param String constraintName:\n
    :return String query:
    """
    query = "ALTER TABLE " + tableName + \
            "\nDROP CONSTRAINT " + constraintName + ";"
    return query


def addValue(tableName, listOfValues, listOfColumns=[]):
    """
    DOESNT EXECUTE A QUERY. Only returns SQL query\n
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


def changeValue(tableName, columnName, newValue, conditionWhere=""):
    """
    DOESNT EXECUTE A QUERY. Only returns SQL query\n
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


def deleteValue(tableName, conditionWhere):
    """
    DOESNT EXECUTE A QUERY. Only returns SQL query\n
    Delete values from table with specified conditionWhere.\n
    :param String tableName:\n
    :param String conditionWhere:\n
    :return String query:
    """
    query = "DELETE FROM " + tableName + \
            "\nWHERE " + conditionWhere + ";"
    return query


def getValue(tableName, listOfColumns=[], conditionWhere=""):
    """
    DOESNT EXECUTE A QUERY. Only returns SQL query\n
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
#       TODO: Сделать создание SELECT'а с JOIN'ами
#       TODO: Сделать добавление внешнего ключа
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
