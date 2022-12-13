from bs4 import BeautifulSoup
import requests
from tkinter import *
from time import sleep
from tkinter import Tk

def rankbot_activation():
    try:
        u = Username.get()
        name = 'https://op.gg/summoners/na/' + u
        source = requests.get(name,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}).text
        soup = BeautifulSoup(source, "html.parser")
        lp = soup.find("div", {"class": "lp"}).getText()
        rank = soup.find("div", {"class": "tier"}).getText()
        print(str(rank).replace("\t", ""), str(lp).replace("\t", ""))
    except:
        print("There is no account of this name or the summoner is unranked")
master = Tk()
Label(master, text="Username").grid(row=0)
Username = Entry(master)
Username.grid(row=0, column=1)
Button(master, text='Quit', command=master.quit).grid(row=1, column=0, sticky=W, pady=4)
Button(master, text='Activate webbot', command=rankbot_activation).grid(row=1, column=1, sticky=W, pady=4)
mainloop()