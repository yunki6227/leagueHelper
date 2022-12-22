import findChampion
import opggReader
import imageCapture
import time
def main():
    names = findChampion.getChampionNames()
    if not imageCapture.isTopMyTeam:
        for i in range(5):
            temp=names[i]
            names[i]=names[i+5]
            names[i+5]=temp
    opggReader.getTeamWinrate(names)
    return 0

time.sleep(2)
main()