import psycopg2
import pandas as pd


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


if __name__ == "__main__":
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(dbname='PythonLabs', user='postgres',
                                      password='python', host='localhost')
        connection.autocommit = True
        cursor = connection.cursor()
    except:
        print("Ошибка соединения с базой данных!")
        exit()

    cursor.execute("CREATE TABLE IF NOT EXISTS firm "
                   "(id integer NOT NULL PRIMARY KEY,"
                   "\ntitle character varying(100) NOT NULL);")
    connection.commit()
    cursor.execute("CREATE TABLE IF NOT EXISTS function "
                   "(id integer NOT NULL PRIMARY KEY,"
                   "\ntitle character varying(100) NOT NULL);")
    connection.commit()
    cursor.execute("CREATE TABLE IF NOT EXISTS person "
                   "(id integer NOT NULL PRIMARY KEY,"
                   "\nfullname character varying(100) NOT NULL,"
                   "\nage integer NOT NULL,"
                   "\nsex character varying(10) NOT NULL,"
                   "\nid_firm integer NOT NULL,"
                   "\nid_function integer NOT NULL);")
    connection.commit()

    print("Задание №1: ")
    cursor.execute("SELECT firm.title, COUNT(*) as number_of_persons"
                   "\nFROM firm JOIN person ON (firm.id = person.id_firm)"
                   "\nWHERE person.age BETWEEN 20 AND 30"
                   "\nGROUP BY firm.title"
                   "\nORDER BY number_of_persons DESC"
                   "\nLIMIT 1;")
    values = cursor.fetchall()
    print(listToPandas(["Название фирмы", "Количество человек"], values))

    print("Задание №2: ")
    cursor.execute("SELECT person.fullname"
                   "\nFROM person JOIN function ON (person.id_function = function.id)"
                   "\nJOIN firm ON (person.id_firm = firm.id)"
                   "\nWHERE function.title = 'Директор' AND firm.title = 'НосковИко';")
    values = cursor.fetchall()
    print(listToPandas(["ФИО директора НосковИко"], values))
