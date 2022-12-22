# contains methods that scrape data from op.gg
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

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
    elif laneNum == 2:
        lane = "mid"
    elif laneNum == 3:
        lane = "adc"
    else:
        lane = "support"
    
    driver = webdriver.Chrome()
    driver.get("https://www.op.gg/champions/"+champion1+"/"+lane+"/counters?region=global&tier=all&target_champion="+champion2)
    source = driver.page_source
    soup = BeautifulSoup(source,"html.parser")
    winrate = soup.find("span",{"class":"percent"}).getText()
    winrate = float(winrate.replace('%',''))
    return winrate

# def getTeamWinrateOverTime():

# def getChampWinrateOverTime():

# def getTeamItemRecommended():

# def getChampItemRecommended(champion1,champion2):

# def getTeamRuneRecommended():

# def getChampRuneRecommended(champion1,champion2):
