#Tarkov Script
import tkinter as tk
from tkinter import *
from tkinter.font import *
import skill.endurance
import skill.covert
import skill.death
import heal.noheal
import heal.nohpheal
import heal.fullheal
import map.shoreline
import map.customs
import map.factory
import map.interchange
import map.lighthouse
import map.reserve
import map.streets
import map.woods

import base64, PIL, requests
from PIL import ImageTk



#Main Window
m = tk.Tk()
m.title("Tarkov Botting Script")

raw_data = requests.get("https://i.imgur.com/cOilDmS.png", stream=True)
image = PhotoImage(data=raw_data.content)

m.tk.call('wm', 'iconphoto', m._w, image)


m.geometry("300x200")
m.configure(bg="black")

#Map Selection
maptitle = Label(m, text='Choose a map to run:', bg="black",fg="#f07a3c",font=Font(size=12))
maptitle.pack(pady=1)
maps = ["Shoreline","Woods","Customs","Factory","Interchange","Lighthouse","Reserve","Streets Of Tarkov"]
mapname = StringVar()
mapname.set("Shoreline")
w = tk.OptionMenu(m,mapname, *maps)
w.config(bg='#f07a3c',highlightthickness=0, highlightcolor="#f07a3c", highlightbackground="#f07a3c")
w.pack()

#Healing Options
Healtitle = Label(m, text='Choose a healing option:', bg="black",fg="#f07a3c",font=Font(size=12))
Healtitle.pack(pady=1)
Healing = ["Full Heal","Only Heal breaks/bleeds","Don't Heal"]
healingop = StringVar()
healingop.set("Full Heal")
h = tk.OptionMenu(m,healingop, *Healing)
h.config(bg='#f07a3c',highlightthickness=0, highlightcolor="#f07a3c", highlightbackground="#f07a3c")
h.pack()

#Skill Options
skilltitle = Label(m, text='Choose a skill to level:', bg="black",fg="#f07a3c",font=Font(size=12))
skilltitle.pack(pady=1)
Skills = ["Endurance/Strength","Covert","Death, heavy bleeds required"]
skillop = StringVar()
skillop.set("Endurance/Strength")
s = tk.OptionMenu(m,skillop, *Skills)
s.config(bg='#f07a3c',highlightthickness=0, highlightcolor="#f07a3c", highlightbackground="#f07a3c")
s.pack()

#Commands
def startBot():
    mapSel = mapname.get()
    healSel = healingop.get()
    skillSel = skillop.get()

    if mapSel == "Shoreline":
        map.shoreline.run()
        if healSel == "Full Heal":
            heal.fullheal.run()
            if skillSel == "Endurance/Strength":
                skill.endurance.run()
            elif skillSel == "Covert":
                skill.covert.run()
            elif skillSel == "Death, heavy bleeds required":
                skill.death.run()
            else:
                print("Broke after Skill Select")
        elif healSel == "Only Heal breaks/bleeds":
            heal.nohpheal.run()
            if skillSel == "Endurance/Strength":
                skill.endurance.run()
            elif skillSel == "Covert":
                skill.covert.run()
            elif skillSel == "Death, heavy bleeds required":
                skill.death.run()
            else:
                print("Broke after Skill Select")
        elif healSel == "Don't Heal":
            heal.noheal.run()
            if skillSel == "Endurance/Strength":
                skill.endurance.run()
            elif skillSel == "Covert":
                skill.covert.run()
            elif skillSel == "Death, heavy bleeds required":
                skill.death.run()
            else:
                print("Broke after Skill Select")
        else:
            print("Broke after Heal Select")

    elif mapSel == "Woods":
        if healSel == "Full Heal":
            heal.fullheal.run()
            if skillSel == "Endurance/Strength":
                skill.endurance.run()
            elif skillSel == "Covert":
                skill.covert.run()
            elif skillSel == "Death, heavy bleeds required":
                skill.death.run()
            else:
                print("Broke after Skill Select")
        elif healSel == "Only Heal breaks/bleeds":
            heal.nohpheal.run()
            if skillSel == "Endurance/Strength":
                skill.endurance.run()
            elif skillSel == "Covert":
                skill.covert.run()
            elif skillSel == "Death, heavy bleeds required":
                skill.death.run()
            else:
                print("Broke after Skill Select")
        elif healSel == "Don't Heal":
            heal.noheal.run()
            if skillSel == "Endurance/Strength":
                skill.endurance.run()
            elif skillSel == "Covert":
                skill.covert.run()
            elif skillSel == "Death, heavy bleeds required":
                skill.death.run()
            else:
                print("Broke after Skill Select")
        else:
            print("Broke after Heal Select")
    elif mapSel == "Customs":
        if healSel == "Full Heal":
            heal.fullheal.run()
            if skillSel == "Endurance/Strength":
                skill.endurance.run()
            elif skillSel == "Covert":
                skill.covert.run()
            elif skillSel == "Death, heavy bleeds required":
                skill.death.run()
            else:
                print("Broke after Skill Select")
        elif healSel == "Only Heal breaks/bleeds":
            heal.nohpheal.run()
            if skillSel == "Endurance/Strength":
                skill.endurance.run()
            elif skillSel == "Covert":
                skill.covert.run()
            elif skillSel == "Death, heavy bleeds required":
                skill.death.run()
            else:
                print("Broke after Skill Select")
        elif healSel == "Don't Heal":
            heal.noheal.run()
            if skillSel == "Endurance/Strength":
                skill.endurance.run()
            elif skillSel == "Covert":
                skill.covert.run()
            elif skillSel == "Death, heavy bleeds required":
                skill.death.run()
            else:
                print("Broke after Skill Select")
        else:
            print("Broke after Heal Select")
    elif mapSel == "Factory":
        if healSel == "Full Heal":
            heal.fullheal.run()
            if skillSel == "Endurance/Strength":
                skill.endurance.run()
            elif skillSel == "Covert":
                skill.covert.run()
            elif skillSel == "Death, heavy bleeds required":
                skill.death.run()
            else:
                print("Broke after Skill Select")
        elif healSel == "Only Heal breaks/bleeds":
            heal.nohpheal.run()
            if skillSel == "Endurance/Strength":
                skill.endurance.run()
            elif skillSel == "Covert":
                skill.covert.run()
            elif skillSel == "Death, heavy bleeds required":
                skill.death.run()
            else:
                print("Broke after Skill Select")
        elif healSel == "Don't Heal":
            heal.noheal.run()
            if skillSel == "Endurance/Strength":
                skill.endurance.run()
            elif skillSel == "Covert":
                skill.covert.run()
            elif skillSel == "Death, heavy bleeds required":
                skill.death.run()
            else:
                print("Broke after Skill Select")
        else:
            print("Broke after Heal Select")
    elif mapSel == "Interchange":
        if healSel == "Full Heal":
            heal.fullheal.run()
            if skillSel == "Endurance/Strength":
                skill.endurance.run()
            elif skillSel == "Covert":
                skill.covert.run()
            elif skillSel == "Death, heavy bleeds required":
                skill.death.run()
            else:
                print("Broke after Skill Select")
        elif healSel == "Only Heal breaks/bleeds":
            heal.nohpheal.run()
            if skillSel == "Endurance/Strength":
                skill.endurance.run()
            elif skillSel == "Covert":
                skill.covert.run()
            elif skillSel == "Death, heavy bleeds required":
                skill.death.run()
            else:
                print("Broke after Skill Select")
        elif healSel == "Don't Heal":
            heal.noheal.run()
            if skillSel == "Endurance/Strength":
                skill.endurance.run()
            elif skillSel == "Covert":
                skill.covert.run()
            elif skillSel == "Death, heavy bleeds required":
                skill.death.run()
            else:
                print("Broke after Skill Select")
        else:
            print("Broke after Heal Select")
    elif mapSel == "Lighthouse":
        if healSel == "Full Heal":
            heal.fullheal.run()
            if skillSel == "Endurance/Strength":
                skill.endurance.run()
            elif skillSel == "Covert":
                skill.covert.run()
            elif skillSel == "Death, heavy bleeds required":
                skill.death.run()
            else:
                print("Broke after Skill Select")
        elif healSel == "Only Heal breaks/bleeds":
            heal.nohpheal.run()
            if skillSel == "Endurance/Strength":
                skill.endurance.run()
            elif skillSel == "Covert":
                skill.covert.run()
            elif skillSel == "Death, heavy bleeds required":
                skill.death.run()
            else:
                print("Broke after Skill Select")
        elif healSel == "Don't Heal":
            heal.noheal.run()
            if skillSel == "Endurance/Strength":
                skill.endurance.run()
            elif skillSel == "Covert":
                skill.covert.run()
            elif skillSel == "Death, heavy bleeds required":
                skill.death.run()
            else:
                print("Broke after Skill Select")
        else:
            print("Broke after Heal Select")
    elif mapSel == "Reserve":
        if healSel == "Full Heal":
            heal.fullheal.run()
            if skillSel == "Endurance/Strength":
                skill.endurance.run()
            elif skillSel == "Covert":
                skill.covert.run()
            elif skillSel == "Death, heavy bleeds required":
                skill.death.run()
            else:
                print("Broke after Skill Select")
        elif healSel == "Only Heal breaks/bleeds":
            heal.nohpheal.run()
            if skillSel == "Endurance/Strength":
                skill.endurance.run()
            elif skillSel == "Covert":
                skill.covert.run()
            elif skillSel == "Death, heavy bleeds required":
                skill.death.run()
            else:
                print("Broke after Skill Select")
        elif healSel == "Don't Heal":
            heal.noheal.run()
            if skillSel == "Endurance/Strength":
                skill.endurance.run()
            elif skillSel == "Covert":
                skill.covert.run()
            elif skillSel == "Death, heavy bleeds required":
                skill.death.run()
            else:
                print("Broke after Skill Select")
        else:
            print("Broke after Heal Select")
    elif mapSel == "Streets Of Tarkov":
        if healSel == "Full Heal":
            heal.fullheal.run()
            if skillSel == "Endurance/Strength":
                skill.endurance.run()
            elif skillSel == "Covert":
                skill.covert.run()
            elif skillSel == "Death, heavy bleeds required":
                skill.death.run()
            else:
                print("Broke after Skill Select")
        elif healSel == "Only Heal breaks/bleeds":
            heal.nohpheal.run()
            if skillSel == "Endurance/Strength":
                skill.endurance.run()
            elif skillSel == "Covert":
                skill.covert.run()
            elif skillSel == "Death, heavy bleeds required":
                skill.death.run()
            else:
                print("Broke after Skill Select")
        elif healSel == "Don't Heal":
            heal.noheal.run()
            if skillSel == "Endurance/Strength":
                skill.endurance.run()
            elif skillSel == "Covert":
                skill.covert.run()
            elif skillSel == "Death, heavy bleeds required":
                skill.death.run()
            else:
                print("Broke after Skill Select")
        else:
            print("Broke after Heal Select")
    else:
        print("Broke during Map Select")

def stopBot():
    print('Stopping the bot!')
    return

#Buttons
frame = Frame(m, bg="black")
frame.pack()
startbutton = Button(frame, text = 'Start', command = startBot)
startbutton.config(bg='#f07a3c',highlightthickness=0, highlightcolor="#f07a3c", highlightbackground="#f07a3c")
startbutton.pack(side = LEFT,pady=5)
stopbutton = Button(frame, text = 'Stop', command= stopBot)
stopbutton.config(bg='#f07a3c',highlightthickness=0, highlightcolor="#f07a3c", highlightbackground="#f07a3c")
stopbutton.pack(padx=10,pady=5)


#Start it
m.mainloop()