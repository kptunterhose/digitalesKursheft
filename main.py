#! /usr/bin/env python
# -*- coding:utf-8 -*-
import copy
import tkinter
from tkinter import *
from tkinter import ttk
from screeninfo import get_monitors

import os
import json
#from collections import namedtuple #für named tuple nt = namedtuble('bla', 'bla bla bla')


RAEUME = ['54', '48', '49a', 'A', 'C', 'D']
STATI = {
    'Klasse erstellen': 0,
    'Klasse bearbeiten': 1,
    'SuS bearbeiten': 2
}
STATUS = 0
AKTIVESUS = set()

GESAMTNAME = dict()


class getNameForPlace(object):

    def __init__(self, klassenfenster):
        self.nameDict = {}
        self.popUp = Toplevel(klassenfenster)
        self.popUp.focus_force()
        Label(self.popUp, text='Vorname').grid(row=0, column=0)
        Label(self.popUp, text='Name').grid(row=1, column=0)
        self.vorname = ttk.Entry(self.popUp)
        self.name = ttk.Entry(self.popUp)
        self.vorname.grid(row=0, column=1)
        self.vorname.focus_set()
        self.name.grid(row=1, column=1)
        self.okayButton = Button(self.popUp, text='okay', command=self.returnNameForPlace)
        self.okayButton.grid(row=2, column=0)
        self.abbrechenButton = Button(self.popUp, text='Abbrechen', command=self.popUp.destroy)
        self.abbrechenButton.grid(row=2, column=1)
        self.popUp.bind('<Return>', self.returnNameForPlace)

    def returnNameForPlace(self,event=None):
        global GESAMTNAME
        GESAMTNAME = ''
        self.nameDict['vorname'] = self.vorname.get()
        self.nameDict['name'] = self.name.get()
        GESAMTNAME = self.nameDict['vorname'] + ' ' + self.nameDict['name']
        self.popUp.destroy()
        pass


def getPos(t, bild=(60, 90)):
    b = bild[0]
    h = bild[1]
    Tisch = {
        1: (10, 10),                                 # hinten links
        2: (int(4 * (b + 10) + 40), 10),             # hinten rechts
        3: (10, int(60 + 3 * h)),                    # vorne links
        4: (int(4 * (b + 10) + 40), int(60 + 3 * h)) # vorne rechts
    }
    Platz = {
        1: (0, 0),
        2: (int(b + 10), 0),
        3: (int(2 * (b + 10)), 0),
        4: (int(3 * (b + 10)), 0),
        5: (int(1 * (b + 10)), int(h + 10)),
        6: (int(2 * (b + 10)), int(h + 10)),
        7: (int(1 * (b + 10)), int(2 * (h + 10))),
        8: (int(2 * (b + 10)), int(2 * (h + 10)))
    }
    try:
        tisch = t[0]
        platz = t[1]
    except IndexError as e:
        print(e)
        print('Falsche Positions Angabe')
    x = Tisch[tisch][0] + Platz[platz][0]
    y = Tisch[tisch][1] + Platz[platz][1]
    return (x, y)


def schiessen(fenster):
    fenster.destroy()


def fenstermasse():
    monitors = get_monitors()
    moniDict = []
    hauptmonitor = 0
    for monitor in monitors:
        moniDict.append(eval(str(monitor)))
    for i in range(len(moniDict)):
        if moniDict[i]['x'] == moniDict[i]['y'] and moniDict[i]['x'] == 0:
            hauptmonitor = i
            break
    hight = int(moniDict[hauptmonitor]['height'])
    width = int(moniDict[hauptmonitor]['width'])
    return hight, width


class VirtuellerKlassenraum(object):
    breite_monitor = 0
    hoehe_monitor = 0
    breite_fenster = 0
    hoehe_fenster = 0
    fenster = Tk()
    sus = {}

    def __init__(self):
        self.fenster.wait_visibility(self.fenster)
        self.fenster.resizable(0, 0)
        self.fenster.wm_attributes("-alpha", 1)
        self.fenster.title('Klasse XY')

        self.hoehe_monitor = self.fenster.winfo_screenheight()
        self.breite_monitor = self.fenster.winfo_screenwidth()
        self.breite_fenster = 1000
        self.hoehe_fenster = 630

        xpos_fenster = 0
        ypos_fenster = 000
        geo_fenster = str(self.breite_fenster) + 'x' + str(self.hoehe_fenster) \
                      + '+' + str(xpos_fenster) + '+' + str(ypos_fenster)
        self.fenster.geometry(geo_fenster)  # breitexhöhe+y-offset+x-offset

        self.klasseLaden = Button(self.fenster, text='Klasse laden')
        self.klasseLaden.place(x=700, y=10, width=120)
        self.speichern = Button(self.fenster, text='speichern')
        self.speichern.place(x=700, y=50, width=120)
        self.neueKlasse = Button(self.fenster, text='neue Klasse')
        self.neueKlasse.place(x=700, y= 90, width=120)
        self.thema = Label(self.fenster, text='Thema der Stunde')
        self.thema.place(x=700, y=140, width=120)
        self.benutzer = Entry(self.fenster)  # Kaffeetasse show=u'\u2615'
        # self.passwort = Entry(self.fenster)  # Atom show=u'\u269B'
        self.benutzer.place(x=700, y=170, width=120)
        self.mitarbeitGut = Button(self.fenster, text='+')
        self.mitarbeitGut.place(x=700, y=210, width=30)
        self.mitarbeitGut['state'] = tkinter.DISABLED
        self.mitarbeitMittel = Button(self.fenster, text='o')
        self.mitarbeitMittel.place(x=740, y=210, width=30)
        self.mitarbeitMittel['state'] = tkinter.DISABLED
        self.mitarbeitSchlecht = Button(self.fenster, text='-')
        self.mitarbeitSchlecht.place(x=780, y=210, width=30)
        self.mitarbeitSchlecht['state'] = tkinter.DISABLED
        #sus einlesen
        all = {}
        id = 0
        for i in range(1, 5):
            for j in range(1, 9):
                id += 1
                all[id] = SuS(name=str(id), stufe='8', raum='54', pos=(i, j), fenster=self.fenster)

    def bewerten(self, n):
        print(n)
        self.mitarbeitGut['state'] = tkinter.NORMAL
        self.mitarbeitMittel['state'] = tkinter.NORMAL
        self.mitarbeitSchlecht['state'] = tkinter.NORMAL

    def ladeKlasse(self):
        pass

    def neueKlasse(self):
        pass


class SuS(object):
    raum = ''
    platz = dict()
    platz[raum] = (0, 0)
    name = ''
    bild = '' # path to file
    stufe = 0 # 5-13 (11=EF; 12=Q1; 13=Q2)
    muendlichBool = False
    isActive = False

    def __init__(self, name, stufe, raum, pos, muendlichBool=True, bild='', fenster=''):
        # stufe: 5 bis 13
        # bild: Pfad zur Datei
        self.name = name
        self.stufe = stufe
        self.raum = raum
        self.platz = dict()
        self.platz[self.raum] = pos
        self.muendlichBool = muendlichBool
        self.bild = bild
        self.button = Button(fenster, text=name, wraplength=50)
        self.button.place(x=getPos(self.platz[self.raum])[0],
                          y=getPos(self.platz[self.raum])[1], width=60, height=90)
        self.button.configure(command=self.doStuff)
        self.fenster=fenster

    def doStuff(self):
        global AKTIVESUS, GESAMTNAME
        self.isActive = not (self.isActive)
        if self.isActive:
            self.button.configure(bg='yellow')
            AKTIVESUS.add(self.name)
            if STATUS == STATI['Klasse erstellen']:
                test = getNameForPlace(self.fenster)
                test.okayButton.wait_window(test.popUp)
                anzeigeName = GESAMTNAME
                self.button.configure(text=anzeigeName)
                AKTIVESUS.remove(self.name)
                self.button.configure(bg='SystemButtonFace')
        else:
            self.button.configure(bg='SystemButtonFace')
            AKTIVESUS.remove(self.name)
        print(AKTIVESUS)

    def umsetzten(self, posNeu):
        pass

    def umwaehlen(self, muendlichBoolNeu):
        pass

    def addBild(self, bild):
        pass



if __name__ == '__main__':
    vk = VirtuellerKlassenraum()
    vk.fenster.mainloop()
