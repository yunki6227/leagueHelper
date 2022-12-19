import sqlite3

import championSkinDataReader


def connect():
    connection=sqlite3.connect(r"resource\leagueChampSkins.sqlite3")
    cursor = connection.cursor()
    try:
        query = "SELECT * FROM skins"
        cursor.execute(query)
    except sqlite3.OperationalError:
        createTables(connection)
    return connection

def reset(connection):
    cursor = connection.cursor()
    query = "DROP skins"
    cursor.execute(query)
    connection = None

def createTables(connection):
    cursor = connection.cursor()
    query = "CREATE TABLE IF NOT EXISTS skins (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, skin_name VARCHAR(255) NOT NULL, champion_name VARCHAR(255) NOT NULL);"
    cursor.execute(query)

# uses method from championSkinDataReader to fill data up in sqlite3
def populateData(connection):
    arraySkinChamp=championSkinDataReader.getSkinInfos()
    cursor = connection.cursor()
    for skin in arraySkinChamp:
        query = "INSERT INTO skins (skin_name,champion_name) VALUES(\""+skin[0]+"\",\""+skin[1]+"\");"
        cursor.execute(query)
    connection.commit()
    
    
connection = connect()
populateData(connection)