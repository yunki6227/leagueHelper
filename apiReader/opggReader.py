# contains methods that scrape data from op.gg
import requests
from bs4 import BeautifulSoup

def getTeamWinrate(names):
    try:
        totalWinrate=0
        for i in range(5):
            totalWinrate+=getChampWinrate(names[i],names[i+5],i)
        return round(totalWinrate/5,2)
    except:
        print("Error in obtaining champion(s) winrate(s)")   
def getChampWinrate(champion1,champion2,laneNum):
    lane=""
    if laneNum == 0:
        lane = "top"
    elif laneNum == 1:
        lane = "jungle"


# def getTeamWinrateOverTime():

# def getChampWinrateOverTime():

# def getTeamItemRecommended():

# def getChampItemRecommended(champion1,champion2):

# def getTeamRuneRecommended():

# def getChampRuneRecommended(champion1,champion2):
