from time import sleep
import pyautogui
import snp
from PIL import ImageOps
import numpy as np
import pyscreenshot as ImageGrab

box=(595, 925, 790, 930)
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


dino = snp.locateOnScreen("/home/wan/Desktop/pythonHW/dino.png")
'''
if dino !=None:
    print dino
'''


while 1:
    tree = snp.locateOnScreen("/home/wan/Desktop/pythonHW/tree.png")
    if tree != None:
        print tree
        pyautogui.press('space')
    else:
        1==1
