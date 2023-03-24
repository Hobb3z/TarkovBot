#Tarkov Script
import tkinter as tk
from tkinter import *
from tkinter.font import *

m = tk.Tk()
m.title("Tarkov Botting Script")
m.iconbitmap("finally.ico")
m.geometry("300x200")
m.configure(bg="#71797E")

#Map Selection
maptitle = Label(m, text='Choose a map to run:', bg="#71797E",fg="white",font=Font(size=12))
maptitle.pack(pady=1)
maps = ["Shoreline","Woods","Customs","Factory","Interchange","Lighthouse","Reserve","Streets Of Tarkov"]
w = tk.Spinbox(m, values=maps,font=Font(size=12),state = 'readonly')
w.pack()

#Healing Options
Healtitle = Label(m, text='Choose a healing option:', bg="#71797E",fg="white",font=Font(size=12))
Healtitle.pack(pady=1)
Healing = ["Full Heal","Only Heal breaks/bleeds","Don't Heal"]
h = tk.Spinbox(m, values=Healing,font=Font(size=12),state = 'readonly')
h.pack()

#Skill Options
skilltitle = Label(m, text='Choose a skill to level:', bg="#71797E",fg="white",font=Font(size=12))
skilltitle.pack(pady=1)
Skills = ["Endurance/Strength","Covert","Death, heavy bleeds required"]
s = tk.Spinbox(m, values=Skills,font=Font(size=12),state = 'readonly')
s.pack()

#Commands
def startBot():
    return

def stopBot():
    return


#Buttons
frame = Frame(m, bg="#71797E")
frame.pack()
startbutton = Button(frame, text = 'Start', command = startBot)
startbutton.pack(side = LEFT,pady=5)
stopbutton = Button(frame, text = 'Stop', command= stopBot)
stopbutton.pack(padx=10,pady=5)


#Start it
m.mainloop()