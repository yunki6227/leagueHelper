import findChampion
import opggReader
import champDatabaseManager
import time
def main():
    names = findChampion.getChampionNames()
    opggReader.getTeamWinrate(names)
    return 0

time.sleep(2)
main()