import sqlite3

connection = None

def connect():
    if connection is None:
        connection=sqlite3.connect("leagueChampSkins.sqlite3")
    createTables()

def reset():
    if connection is None:
        return 0
    cursor = connection.cursor()
    query = "DROP skins"
    cursor.execute(query)
    connection = None

def createTables():
    cursor = connection.cursor()
    query = "CREATE TABLE IF NOT EXISTS skins (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, skin_name VARCHAR(255) NOT NULL, champion_name VARCHAR(255) NOT NULL);"
    cursor.execute(query)

def populateData():
    # uses method from championSkinDataReader to fill data up in sqlite3
    