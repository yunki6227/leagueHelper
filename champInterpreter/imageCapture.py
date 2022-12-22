import pyautogui
import time
# Captures images for each champion's name, like Octoberfest Gragas, for each player in loading screen
# return some data with image information and player information, perhaps in a tuple (player,image)
# Example: (top1, image_top1) would mean top player from team 1, and its corresponding image
# could continue like top1,top2,jg1,jg2,mid1,mid2,adc1,adc2,sup1,sup2


# calls captureImage 10 times to capture 
def captureNames():
    images=[]
    x=242 #x coordinate for leftmost champion name
    y=400 #y coordinate for top team champions' names
    width=250 #width of name
    height=20 #height of name
    time.sleep(2)
    for i in range(5):
        images.append(captureImage(x,y,width,height))
        x+=296
    y=935 #set y coordinate for bottom team names
    x=242 #reset x coordinate to face leftmost champion
    for i in range(5):
        images.append(captureImage(x,y,width,height))
        x+=296
    return images

def captureImage(x,y,width,height):
    return pyautogui.screenshot(region=(x,y,width,height))