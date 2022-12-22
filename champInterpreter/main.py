import findChampion
import opggReader
import time
def main():
    names = findChampion.getChampionNames()
    opggReader.getTeamWinrate(names)


time.sleep(2)
main()