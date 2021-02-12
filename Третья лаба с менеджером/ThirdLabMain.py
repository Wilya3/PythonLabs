import ThirdLabSQLInterface
import SQLQueryManager


def createTable(db):
    tableName = askTableName()
    print("Введите количество столбцов")
    numberOfColumns = int(input())
    listOfColumnNames = []
    listOfColumnTypesAndNullDefault = []
    for i in range(numberOfColumns):
        listOfColumnNames.append(askColumnName())
        listOfColumnTypesAndNullDefault.append(askColumnTypeAndNullDefault())
    print("Введите через пробел названия столбцов с первичным ключом")
    listOfPKColumns = input().split(" ")
    query = SQLQueryManager.createTable(tableName, listOfColumnNames,
                                        listOfColumnTypesAndNullDefault, listOfPKColumns)
    db.sdelatzapros(query)

def deleteTable(db):
    tableName = askTableName()
    query = SQLQueryManager.dropTable(tableName)
    db.sdelatzapros(query)

def addConstraint(db):
    tableName = askTableName()
    constraintName = askConstraintName()
    print("Выберите тип ограничения (check, unique)")
    type = input().lower()
    if type == "check":
        print("Введите условие ограничения (Price > 1000 AND year > 2013)")
        condition = input()
        query = SQLQueryManager.addConstraintCheck(tableName, constraintName, condition)
        db.sdelatzapros(query)
    elif type == "unique":
        columnName = askColumnName()
        query = SQLQueryManager.addConstraintUnique(tableName, constraintName, columnName)
        db.sdelatzapros(query)
    else:
        print("Ошибка ввода типа ограничения")
        return

def dropConstraint(db):
    tableName = askTableName()
    constraintName = askConstraintName()
    query = SQLQueryManager.dropConstraint(tableName, constraintName)
    db.sdelatzapros(query)

def addColumn(db):
    tableName = askTableName()
    columnName = askColumnName()
    columnType = askColumnTypeAndNullDefault()
    query = SQLQueryManager.addColumn(tableName, columnName, columnType)
    db.sdelatzapros(query)

def dropColumn(db):
    tableName = askTableName()
    columnName = askColumnName()
    query = SQLQueryManager.dropColumn(tableName, columnName)
    db.sdelatzapros(query)

def addValue(db):
    tableName = askTableName()
    listOfColumnNames = askColumns()
    print("Введите значения через пробел. Для текстовых значений используйте одинарные кавычки")
    print("Пример: 'Иванов' 'Иван' 'Иванович' 87001234567")
    listOfValues = input().split(" ")
    query = SQLQueryManager.addValue(tableName, listOfValues, listOfColumnNames)
    db.sdelatzapros(query)

def deleteValue(db):
    tableName = askTableName()
    print("Введите условие удаления (Price > 1000 AND year > 2013)")
    condition = input()
    query = SQLQueryManager.deleteValue(tableName, condition)
    db.sdelatzapros(query)

def changeValue(db):
    tableName = askTableName()
    columnName = askColumnName()
    print("Введите новое значение")
    newValue = input()
    print("Введите условие удаления")
    condition = ""
    condition += input()  # TODO: Проверить ошибки
    query = SQLQueryManager.changeValue(tableName, columnName, newValue, condition)
    db.sdelatzapros(query)

def getValue(db):
    tableName = askTableName()
    listOfColumnNames = askColumns()
    print("Введите условие, если необходимо ")
    print("или не вводите ничего для получения всех строк")
    condition = input()
    query = SQLQueryManager.getValue(tableName, listOfColumnNames, condition)
    db.sdelatzapros(query)

def closeAndExit(db):
    db.close()
    exit()

def
def askTableName():
    print("Введите название таблицы")
    return input()

def askConstraintName():
    print("Введите название ограничения")
    return input()

def askColumnName():
    print("Введите название столбца")
    return input()

def askColumnTypeAndNullDefault():
    print("Введите тип столбца и, если необходимо, DEFAULT, NOT NULL характеристики")
    print("Пример: CHARACTER VARYING(10) NOT NULL")
    return input()

def askColumns():
    listOfColumnNames = []
    print("Введите через пробел названия столбцов "
          "\nили не вводите ничего для работы со всеми столбцами")
    inputString = input()
    if len(inputString) > 0:
        listOfColumnNames = inputString.split(" ")
    return listOfColumnNames


if __name__ == "__main__":
    db = ThirdLabSQLInterface.SQLInterface
    commands = {"create table": createTable(db),
                "delete table": deleteTable(db),
                "add constraint": addConstraint(db),
                "delete constraint": dropConstraint(db),
                "add column": addColumn(db),
                "delete column": dropColumn(db),
                "add values": addValue(db),
                "delete values": deleteValue(db),
                "change values": changeValue(db),
                "get values": getValue(db),
                "exit": closeAndExit(db),
                }
    while True:
        print("Какое действие необходимо?")
        for key in commands:
            print("\n" + key)
        action = input().lower()
        if commands.get(action) is None:
            print("Неверная команда! Повторите ввод")
            continue
        else:
            try:
                commands.get(action)
            except:
                "Произошла ошибка. Действие отменяется"
        if action == "exit":
            break