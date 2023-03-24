#Tarkov Script
import tkinter as tk
from tkinter import *
from tkinter.font import *


#Main Window
m = tk.Tk()
m.title("Tarkov Botting Script")
#m.iconbitmap("finally.ico")
m.geometry("300x200")
m.configure(bg="#373C49")

#Map Selection
maptitle = Label(m, text='Choose a map to run:', bg="#373C49",fg="white",font=Font(size=12))
maptitle.pack(pady=1)
maps = ["Shoreline","Woods","Customs","Factory","Interchange","Lighthouse","Reserve","Streets Of Tarkov"]
mapname = StringVar()
mapname.set("Shoreline")
w = tk.OptionMenu(m,mapname, *maps)
w.pack()

#Healing Options
Healtitle = Label(m, text='Choose a healing option:', bg="#373C49",fg="white",font=Font(size=12))
Healtitle.pack(pady=1)
Healing = ["Full Heal","Only Heal breaks/bleeds","Don't Heal"]
healingop = StringVar()
healingop.set("Full Heal")
h = tk.OptionMenu(m,healingop, *Healing)
h.pack()

#Skill Options
skilltitle = Label(m, text='Choose a skill to level:', bg="#373C49",fg="white",font=Font(size=12))
skilltitle.pack(pady=1)
Skills = ["Endurance/Strength","Covert","Death, heavy bleeds required"]
skillop = StringVar()
skillop.set("Endurance/Strength")
s = tk.OptionMenu(m,skillop, *Skills)
s.pack()

#Commands
def startBot():
    return

def stopBot():
    return

#Buttons
frame = Frame(m, bg="#373C49")
frame.pack()
startbutton = Button(frame, text = 'Start', command = startBot)
startbutton.pack(side = LEFT,pady=5)
stopbutton = Button(frame, text = 'Stop', command= stopBot)
stopbutton.pack(padx=10,pady=5)


#Start it
m.mainloop()