import math
import pyga
import multitasking
import time
from pystray import MenuItem as item
import pystray
from PIL import Image
import os
from pynput.mouse import Button,Controller
mouse=Controller()
topSpeed=1#8#7.5
accel=0.45#0.15
slowWhileInMotion=False

inUi=False
@multitasking.task
def display():
    global topSpeed
    global inUi
    inUi=True
    typed=str(topSpeed)
    char='0123456789'
    pyga.clicked=None
    pyga.display_init((300,300),name="Mouse Multiply Config")
    while inUi:
        pyga.fill((255,255,255))
        pyga.text('Top Speed: '+str(typed),(0,0),(0,0,0),20)
        key=pyga.getkey()
        if(key!=None and key in char):
            typed+=key
        elif(key=='backspace'):
            typed=typed[:-1]
        pyga.button('Save',(100,50),(70,25),(200,200,200))
        pyga.button('Reset',(100,120),(70,25),(200,200,200))
        if(pyga.clicked==0):
            topSpeed=int(typed)
            inUi=False
        elif(pyga.clicked==1):
            typed=str(2)
            topSpeed=int(typed)
        a=pyga.nocloseupdate()
        if(a=="close"):
            inUi=False
    pyga.quit()

def c_shutdown(icon):
    global inUi
    global stop
    #SysTrayIcon.shutdown(systray)
    inUi=False
    stop=True
    os._exit(os.EX_OK)
    icon.stop()
    exit()

@multitasking.task
def tray():
    image = Image.open("image.jpg")
    menu = (item('Config', display), item('Exit', c_shutdown))
    icon = pystray.Icon("Mouse Multiply", image, "Mouse Multiply", menu)
    icon.run_detached()


tray()
speedM=0
stop=False
pos2=mouse.position
while(stop==False):
    if(inUi==False):
        if(speedM>topSpeed):
            speedM=topSpeed
        speedM=speedM/1.00005
        pos=mouse.position
        if(pos2!=pos):
            try:
                mouse.position=(pos[0]-((pos2[0]-pos[0])*(speedM)),pos[1]-((pos2[1]-pos[1])*(speedM)))
                pos2=mouse.position
                pos=pos2
            except:
                pass
            if(slowWhileInMotion):
                speedM=speedM/1.02
            if(speedM+accel<topSpeed):
                speedM+=accel
            else:
                speedM=topSpeed
    else:
        pos=mouse.position
        pos2=pos
        speedM=0
exit()
