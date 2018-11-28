from time import sleep
import pyautogui
import snp
from PIL import ImageOps
import numpy as np
import pyscreenshot as ImageGrab

box = (755 , 240 , 895 , 250)
box2 = (755 , 233 , 915 , 250)
box3 = (755 , 233 , 947 , 250)
box4 = (755 , 233 , 985 , 250)
box5 = (755 , 233 , 1030 , 250)
box6 = (755 , 233 , 1040 , 250)
'''
while 1:
    x , y = pyautogui.position()

    print x , y
'''
p = snp.locateOnScreen("/home/wan/Desktop/pythonHW/chrome.png")

if p == None:
    print("Do not find Chrome")
else :
    pyautogui.click(p[0]+p[2]//2,p[1]+p[3]//2)

image=ImageGrab.grab(box)
jump_box=ImageOps.grayscale(image)
jump_box=np.array(jump_box.getcolors())
white=jump_box.sum()

image2=ImageGrab.grab(box2)
jump_box2=ImageOps.grayscale(image2)
jump_box2=np.array(jump_box2.getcolors())
white2=jump_box2.sum()

image3=ImageGrab.grab(box3)
jump_box3=ImageOps.grayscale(image3)
jump_box3=np.array(jump_box3.getcolors())
white3=jump_box3.sum()

image4=ImageGrab.grab(box4)
jump_box4=ImageOps.grayscale(image4)
jump_box4=np.array(jump_box4.getcolors())
white4=jump_box4.sum()

image5=ImageGrab.grab(box5)
jump_box5=ImageOps.grayscale(image5)
jump_box5=np.array(jump_box5.getcolors())
white5=jump_box5.sum()

image6=ImageGrab.grab(box6)
jump_box6=ImageOps.grayscale(image6)
jump_box6=np.array(jump_box6.getcolors())
white6=jump_box6.sum()


pyautogui.FAILSAFE =  False
pyautogui.PAUSE = 0
i=0
while True:
    image=ImageGrab.grab(box)
    jump_box=ImageOps.grayscale(image)
    jump_box=np.array(jump_box.getcolors())
    if jump_box.sum() != white:
        pyautogui.press('space')
        #sleep(0.22)
        #pyautogui.press('down')
        i+=1
    if i > 25:
        break;

while True:
    image2=ImageGrab.grab(box2)
    jump_box2=ImageOps.grayscale(image2)
    jump_box2=np.array(jump_box2.getcolors())
    if jump_box2.sum() != white2:
        pyautogui.press('space')
        print("hi")
        sleep(0.26)
        pyautogui.press('down')
        i+=1 
    if i > 55:
        break;

while True:
    image3=ImageGrab.grab(box3)
    jump_box3=ImageOps.grayscale(image3)
    jump_box3=np.array(jump_box3.getcolors())
    if jump_box3.sum() != white3:
        pyautogui.press('space')
        print("yo")
        sleep(0.24)
        pyautogui.press('down')
        i+=1 
    if i>80:
        break

while True:
    image4=ImageGrab.grab(box4)
    jump_box4=ImageOps.grayscale(image4)
    jump_box4=np.array(jump_box4.getcolors())
    if jump_box4.sum() != white4:
        pyautogui.press('space')
        sleep(0.25)
        print("ya")
        pyautogui.press('down')
        i+=1 
    if i >110:
        break


while True:
    image5=ImageGrab.grab(box5)
    jump_box5=ImageOps.grayscale(image5)
    jump_box5=np.array(jump_box5.getcolors())
    if jump_box5.sum() != white5:
        pyautogui.press('space')
        if i <155:
            print("HA")
            sleep(0.21)
        else:
            print("60")
            sleep(0.18)
        pyautogui.press('down')
        i+=1
    if i >200:
        break
    

while True:
    image6=ImageGrab.grab(box6)
    jump_box6=ImageOps.grayscale(image6)
    jump_box6=np.array(jump_box6.getcolors())
    if jump_box6.sum() != white6:
        pyautogui.press('space')
        print("el")
        sleep(0.18)
        pyautogui.press('down')
        i+=1 


