# contains methods that scrape data from op.gg
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def getTeamWinrate(names):
    totalWinrate=0
    driver = getChromeDriverWithOptions()
    for i in range(5):
        lane = getLaneInfoString(i)
        driver.get("https://www.op.gg/champions/"+names[i]+"/"+lane+"/counters?region=global&tier=all&target_champion="+names[i+5])
        source = driver.page_source
        soup = BeautifulSoup(source,"html.parser")
        winrate = soup.find("span",{"class":"percent"})
        if winrate:
            winrate=winrate.getText()
            winrate = float(winrate.replace('%',''))
            print(winrate)
            totalWinrate+=winrate
        else:
            driver.get("https://www.op.gg/champions/"+names[i+5]+"/"+lane+"/counters?region=global&tier=all&target_champion="+names[i])
            source = driver.page_source
            soup = BeautifulSoup(source,"html.parser")
            winrate = soup.find("span",{"class":"percent"}).getText()
            winrate = 100-float(winrate.replace('%',''))
            print(winrate)
            totalWinrate+=winrate        

    print(str(round(totalWinrate/5,2))+"%")
    driver.close()
    return round(totalWinrate/5,2) 

def getLaneInfoString(i):
    lane=""
    if i == 0:
        lane = "top"
    elif i == 1:
        lane = "jungle"
    elif i == 2:
        lane = "mid"
    elif i == 3:
        lane = "adc"
    else:
        lane = "support"
    return lane

def getChromeDriverWithOptions():
    options = webdriver.ChromeOptions()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)
    return driver 

if __name__ == "__main__":
    testNames=['Garen','Rengar','Viego','Zeri','Lux','Irelia','Hecarim','Akali','Jhin','Anivia']
    getTeamWinrate(testNames)

# def getTeamWinrate(names):
#     totalWinrate=0
#     for i in range(5):
#         totalWinrate+=getChampWinrate(names[i],names[i+5],i)
#     print(str(round(totalWinrate/5,2))+"%")
#     return round(totalWinrate/5,2)   

# def getChampWinrate(champion1,champion2,laneNum):
#     lane=""
#     if laneNum == 0:
#         lane = "top"
#     elif laneNum == 1:
#         lane = "jungle"
#     elif laneNum == 2:
#         lane = "mid"
#     elif laneNum == 3:
#         lane = "adc"
#     else:
#         lane = "support"
    
#     driver = webdriver.Chrome()
#     driver.get("https://www.op.gg/champions/"+champion1+"/"+lane+"/counters?region=global&tier=all&target_champion="+champion2)
#     source = driver.page_source
#     soup = BeautifulSoup(source,"html.parser")
#     winrate = soup.find("span",{"class":"percent"})
#     if winrate:
#         winrate=winrate.getText()
#         winrate = float(winrate.replace('%',''))
#         print(winrate)
#         return winrate
#     else:
#         driver.get("https://www.op.gg/champions/"+champion2+"/"+lane+"/counters?region=global&tier=all&target_champion="+champion1)
#         source = driver.page_source
#         soup = BeautifulSoup(source,"html.parser")
#         winrate = soup.find("span",{"class":"percent"}).getText()
#         winrate = 100-float(winrate.replace('%',''))
#         print(winrate)
#         return winrate

# testNames=['Garen','Rengar','Viego','Zeri','Lux','Irelia','Hecarim','Akali','Jhin','Anivia']
# getTeamWinrate(testNames)

# def getTeamWinrateOverTime():

# def getChampWinrateOverTime():

# def getTeamItemRecommended():

# def getChampItemRecommended(champion1,champion2):

# def getTeamRuneRecommended():

# def getChampRuneRecommended(champion1,champion2):
