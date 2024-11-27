import datetime
import tkinter
from tkinter import *
from tkinter import ttk
from utils import getPos


class SuS(object):
    raum = ''
    platz = dict()
    platz[raum] = (0, 0)
    name = ''
    bild = '' # path to file
    stufe = 0 # 5-13 (11=EF; 12=Q1; 13=Q2)
    muendlichBool = False
    isActive = False
    dictForSave = dict()
    benotungsDict = dict()

    def __init__(self, id, name, stufe, raum, pos, muendlichBool=True, bild='', fenster=''):
        global getPos
        # stufe: 5 bis 13
        # bild: Pfad zur Datei
        self.id = id
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

    def updateName(self, name):
        self.name = name
        self.button['text'] = self.name

    def doStuff(self):
        global AKTIVESUS, GESAMTNAME, STATUS, STATI
        global getNameForPlace
        self.isActive = not self.isActive
        if self.isActive:
            self.button.configure(bg='yellow')
            AKTIVESUS.add(self.id)
            if STATUS == STATI['Klasse erstellen']:
                test = getNameForPlace(self.fenster)
                test.okayButton.wait_window(test.popUp)
                anzeigeName = GESAMTNAME
                self.button.configure(text=anzeigeName)
                AKTIVESUS.remove(self.id)
                self.isActive = not self.isActive
                self.name = anzeigeName
                self.button.configure(bg='SystemButtonFace')
            elif STATUS == STATI['neutral']:
                pass
        else:
            self.button.configure(bg='SystemButtonFace')
            AKTIVESUS.remove(self.id)

    def umsetzten(self, posNeu):
        pass

    def umwaehlen(self, muendlichBoolNeu):
        pass

    def addBild(self, bild):
        pass

    def makeDictForSave(self):
        self.dictForSave['Name'] = self.name
        self.dictForSave['Stufe'] = self.stufe
        self.dictForSave['Raum'] = self.raum
        self.dictForSave['Platz'] = self.platz
        self.dictForSave['MuendlichBool'] = self.muendlichBool
        self.dictForSave['Bild'] = self.bild
        self.dictForSave['Benotung'] = self.benotungsDict
        return self.dictForSave

    def benoten(self, note, gewichtung=1, kommentar=''):
        global STUNDENZAL
        tag = str(datetime.datetime.now().date())
        self.benotungsDict[tag] = (note, STUNDENZAL, kommentar)
        print(self.name)
        print(self.note)
        pass