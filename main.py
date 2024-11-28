#! /usr/bin/env python
# -*- coding:utf-8 -*-
import copy
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkcalendar import Calendar
from screeninfo import get_monitors
#from Lernender import SuS
import sys
import json
import datetime
#from collections import namedtuple #für named tuple nt = namedtuble('bla', 'bla bla bla')
try:
    SPEICHERNAME = sys.argv[1]
except:
    pass
B = 63  # Bild/Button-Breite
H = 66  # Bild/Button-Höhe
RAEUME = ['134', '54', '48', '49a', 'A', 'B', 'D', 'ABD']

TISCHE = {
    '54': {  # Physikraum 54
        1: (10, 10),  # hinten links
        2: (int(2 * (B + 10) + 1 * 40), 10),  # hinten rechts
        3: (int(4 * (B + 10) + 2 * 40), 10),  # vorne links
        4: (int(6 * (B + 10) + 3 * 40), 10),  # vorne rechts
    },
    '49a': {  # Chemieraum 49a
        1: (10, 10),                                             # hinten links
        2: (int(3 * (B + 10) + 40), 10),                         # hinten rechts
        3: (10, int(10 + 4 * (H + 10))),                         # vorne links
        4: (int(3 * (B + 10) + 40), int(10 + 4 * (H + 10)))      # vorne rechts
    },
    'A': {
        1: (10, 10),                                             # hinten links
        2: (int(3 * (B + 10) + 40), 10),                         # hinten rechts
        3: (10, int(10 + 4 * (H + 10))),                         # vorne links
        4: (int(3 * (B + 10) + 40), int(10 + 4 * (H + 10)))      # vorne rechts
    },
    '134': {  # Klassenraum
        1: (int(5 * (B + 10) + 10), int(5 * (H + 10) + 10)),
        2: (int(2 * (B + 10) + 10), int(5 * (H + 10) + 10)),
        3: (int(0 * (B + 10) + 10), int(5 * (H + 10) + 10)),
        4: (int(0 * (B + 10) + 10), int(4 * (H + 10) + 10)),
        5: (int(0 * (B + 10) + 10), int(3 * (H + 10) + 10)),
        6: (int(0 * (B + 10) + 10), int(2 * (H + 10) + 10)),
        7: (int(0 * (B + 10) + 10), int(1 * (H + 10) + 10)),
        8: (int(0 * (B + 10) + 10), int(0 * (H + 10) + 10)),
        9: (int(1 * (B + 10) + 10), int(0 * (H + 10) + 10)),
        10: (int(2 * (B + 10) + 10), int(0 * (H + 10) + 10)),
        11: (int(3 * (B + 10) + 10), int(0 * (H + 10) + 10)),
        12: (int(4 * (B + 10) + 10), int(0 * (H + 10) + 10)),
        13: (int(5 * (B + 10) + 10), int(0 * (H + 10) + 10)),
        14: (int(6 * (B + 10) + 10), int(0 * (H + 10) + 10)),
        15: (int(7 * (B + 10) + 10), int(0 * (H + 10) + 10)),
        16: (int(8 * (B + 10) + 10), int(0 * (H + 10) + 10)),
        17: (int(8 * (B + 10) + 10), int(1 * (H + 10) + 10)),
        18: (int(8 * (B + 10) + 10), int(2 * (H + 10) + 10)),
        19: (int(8 * (B + 10) + 10), int(3 * (H + 10) + 10)),
        20: (int(8 * (B + 10) + 10), int(4 * (H + 10) + 10)),
        21: (int(8 * (B + 10) + 10), int(5 * (H + 10) + 10)),
        22: (int(8 * (B + 10) + 10), int(6 * (H + 10) + 10)),
        23: (int(6 * (B + 10) + 10), int(5 * (H + 10) + 10)),
        24: (int(0 * (B + 10) + 10), int(6 * (H + 10) + 10)),
        25: (int(.5 * (B + 10) + 10), int(7 * (H + 10) + 10)),
        26: (int(1.5 * (B + 10) + 10), int(7 * (H + 10) + 10)),
        27: (int(2.5 * (B + 10) + 10), int(7 * (H + 10) + 10)),
        28: (int(3.5 * (B + 10) + 10), int(7 * (H + 10) + 10)),
        29: (int(4.5 * (B + 10) + 10), int(7 * (H + 10) + 10)),
        30: (int(5.5 * (B + 10) + 10), int(7 * (H + 10) + 10)),
        31: (int(6.5 * (B + 10) + 10), int(7 * (H + 10) + 10)),
        32: (int(7.5 * (B + 10) + 10), int(7 * (H + 10) + 10)),
    },
    'ABD': { # alte Räume
        1: (int(0 * (B + 10)), int(0 * (H + 10))),
        2: (int(0 * (B + 10)), int(1 * (H + 10))),
        3: (int(0 * (B + 10)), int(2 * (H + 10))),
        4: (int(0 * (B + 10)), int(3 * (H + 10))),
        5: (int(0 * (B + 10)), int(4 * (H + 10))),
        6: (int(0 * (B + 10)), int(5 * (H + 10))),
        7: (int(0 * (B + 10)), int(6 * (H + 10))),
        8: (int(0 * (B + 10)), int(7 * (H + 10))),
        9: (int(1 * (B + 10)), int(1 * (H + 10))),
        10: (int(2 * (B + 10)), int(1 * (H + 10))),
        11: (int(1 * (B + 10)), int(3 * (H + 10))),
        12: (int(2 * (B + 10)), int(3 * (H + 10))),
        13: (int(1 * (B + 10)), int(5 * (H + 10))),
        14: (int(2 * (B + 10)), int(5 * (H + 10))),
        15: (int(1 * (B + 10)), int(7 * (H + 10))),
        16: (int(2 * (B + 10)), int(7 * (H + 10))),
        17: (int(5 * (B + 10) + 40), int(0 * (H + 10))),
        18: (int(5 * (B + 10) + 40), int(1 * (H + 10))),
        19: (int(5 * (B + 10) + 40), int(2 * (H + 10))),
        20: (int(5 * (B + 10) + 40), int(3 * (H + 10))),
        21: (int(5 * (B + 10) + 40), int(4 * (H + 10))),
        22: (int(5 * (B + 10) + 40), int(5 * (H + 10))),
        23: (int(5 * (B + 10) + 40), int(6 * (H + 10))),
        24: (int(5 * (B + 10) + 40), int(7 * (H + 10))),
        25: (int(3 * (B + 10) + 40), int(1 * (H + 10))),
        26: (int(4 * (B + 10) + 40), int(1 * (H + 10))),
        27: (int(3 * (B + 10) + 40), int(3 * (H + 10))),
        28: (int(4 * (B + 10) + 40), int(3 * (H + 10))),
        29: (int(3 * (B + 10) + 40), int(5 * (H + 10))),
        30: (int(4 * (B + 10) + 40), int(5 * (H + 10))),
        31: (int(3 * (B + 10) + 40), int(7 * (H + 10))),
        32: (int(4 * (B + 10) + 40), int(7 * (H + 10))),
    },
    '48': {
        1: (int(0 * (B + 10)), int(0 * (H + 10))),
        2: (int(1 * (B + 10)), int(0 * (H + 10))),
        3: (int(2 * (B + 10)), int(0 * (H + 10))),
        4: (int(3 * (B + 10)), int(0 * (H + 10))),
        5: (int(4 * (B + 10)), int(0 * (H + 10))),
        6: (int(5 * (B + 10)), int(0 * (H + 10))),
        7: (int(6 * (B + 10)), int(0 * (H + 10))),
        8: (int(7 * (B + 10)), int(0 * (H + 10))),
        9: (int(8 * (B + 10)), int(0 * (H + 10))),
        10: (int(9 * (B + 10)), int(0 * (H + 10))),
        11: (int(2 * (B + 10)), int(3 * (H + 10))),
        12: (int(3 * (B + 10)), int(3 * (H + 10))),
        13: (int(2 * (B + 10)), int(4 * (H + 10))),
        14: (int(3 * (B + 10)), int(4 * (H + 10))),
        15: (int(2 * (B + 10)), int(5 * (H + 10))),
        16: (int(3 * (B + 10)), int(5 * (H + 10))),
        17: (int(2 * (B + 10)), int(6 * (H + 10))),
        18: (int(3 * (B + 10)), int(6 * (H + 10))),
        19: (int(2 * (B + 10)), int(7 * (H + 10))),
        20: (int(3 * (B + 10)), int(7 * (H + 10))),
        21: (int(6 * (B + 10)), int(2 * (H + 10))),
        22: (int(7 * (B + 10)), int(2 * (H + 10))),
        23: (int(6 * (B + 10)), int(3 * (H + 10))),
        24: (int(7 * (B + 10)), int(3 * (H + 10))),
        25: (int(6 * (B + 10)), int(4 * (H + 10))),
        26: (int(7 * (B + 10)), int(4 * (H + 10))),
        27: (int(6 * (B + 10)), int(5 * (H + 10))),
        28: (int(7 * (B + 10)), int(5 * (H + 10))),
        29: (int(6 * (B + 10)), int(6 * (H + 10))),
        30: (int(7 * (B + 10)), int(6 * (H + 10))),
        31: (int(6 * (B + 10)), int(7 * (H + 10))),
        32: (int(7 * (B + 10)), int(7 * (H + 10)))
    }
}
PLATZ = {
    '54': {
        1: (int(0 * (B + 10)), int(0 * (H + 10))),
        2: (int(1 * (B + 10)), int(0 * (H + 10))),
        3: (int(0 * (B + 10)), int(1 * (H + 10))),
        4: (int(1 * (B + 10)), int(1 * (H + 10))),
        5: (int(0 * (B + 10)), int(2 * (H + 10))),
        6: (int(1 * (B + 10)), int(2 * (H + 10))),
        7: (int(0 * (B + 10)), int(3 * (H + 10))),
        8: (int(1 * (B + 10)), int(3 * (H + 10)))
    },
    '49a': {
        1: (int(0 * (B + 10)), int(0 * (H + 10))),
        2: (int(1 * (B + 10)), int(0 * (H + 10))),
        3: (int(0 * (B + 10)), int(1 * (H + 10))),
        4: (int(1 * (B + 10)), int(1 * (H + 10))),
        5: (int(0 * (B + 10)), int(2 * (H + 10))),
        6: (int(1 * (B + 10)), int(2 * (H + 10))),
        7: (int(0 * (B + 10)), int(3 * (H + 10))),
        8: (int(1 * (B + 10)), int(3 * (H + 10)))
    },
    'A': {
        1: (int(0 * (B + 10)), int(0 * (H + 10))),
        2: (int(0 * (B + 10)), int(1 * (H + 10))),
        3: (int(1 * (B + 10)), int(1 * (H + 10))),
        4: (int(2 * (B + 10)), int(1 * (H + 10))),
        5: (int(0 * (B + 10)), int(2 * (H + 10))),
        6: (int(0 * (B + 10)), int(3 * (H + 10))),
        7: (int(1 * (B + 10)), int(3 * (H + 10))),
        8: (int(2 * (B + 10)), int(3 * (H + 10)))
    },
    'ABD': {
        1: (0, 0)
    },
    '134': {
        1: (0, 0)
    },
    '48': {
        1: (0, 0)
    }
}
STATI = {
    'neutral': 0,
    'Klasse erstellen': 1,
    'Klasse bearbeiten': 2,
    'SuS bearbeiten': 3
}
STATUS = 0
AKTIVESUS = set()

GESAMTNAME = dict()
KURSNAME = ''
STUNDENZAHL = 1

ALLDATAINONE = True

DATUM = str(datetime.datetime.now().date())


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

    def returnNameForPlace(self, event=None):
        global GESAMTNAME
        GESAMTNAME = ''
        self.nameDict['vorname'] = self.vorname.get()
        self.nameDict['name'] = self.name.get()
        GESAMTNAME = self.nameDict['vorname'] + ' ' + self.nameDict['name']
        self.popUp.destroy()
        pass


class getInfosForKlasse(object):

    def __init__(self, klassenfenster):
        self.nameDict = {}
        self.popUp = Toplevel(klassenfenster)
        self.popUp.focus_force()
        Label(self.popUp, text='Klasse').grid(row=0, column=0)
        Label(self.popUp, text='Fach').grid(row=1, column=0)
        Label(self.popUp, text='Raum').grid(row=2, column=0)
        self.klasse = ttk.Entry(self.popUp)
        self.fach = ttk.Entry(self.popUp)
        self.raum = ttk.Entry(self.popUp)
        self.klasse.grid(row=0, column=1)
        self.klasse.focus_set()
        self.fach.grid(row=1, column=1)
        self.raum.grid(row=2, column=1)
        self.okayButton = Button(self.popUp, text='okay', command=self.returnKlassenInfos)
        self.okayButton.grid(row=3, column=0)
        self.abbrechenButton = Button(self.popUp, text='Abbrechen', command=self.popUp.destroy)
        self.abbrechenButton.grid(row=3, column=1)
        self.popUp.bind('<Return>', self.returnKlassenInfos)

    def returnKlassenInfos(self):
        global KURSNAME
        KURSNAME = ''
        self.nameDict['klasse'] = self.klasse.get()
        self.nameDict['fach'] = self.fach.get()
        self.nameDict['raum'] = self.raum.get()
        KURSNAME = self.nameDict['klasse'] + '-' + self.nameDict['fach'] + '-' + self.nameDict['raum']
        self.popUp.destroy()
        pass


class getDatum(object):

    def __init__(self, klassenfenster):
        self.topFenster = klassenfenster
        self.popUp = Toplevel(self.topFenster)
        self.popUp.focus_force()
        jahr = datetime.date.today().year
        tag = datetime.date.today().day
        monat = datetime.date.today().month
        self.cal = Calendar(self.popUp,
                       selectmode='day',
                       year=jahr, month=monat, day=tag)
        self.cal.pack(fill='both', expand=True)
        self.okayButton = Button(self.popUp, text='Ok', command=self.getDatum)
        self.okayButton.pack()

    def getDatum(self):
        global DATUM
        DATUM = self.cal.selection_get()
        self.popUp.destroy()


def getPos(t, raum='49a'):
    try:
        tisch = t[0]
        platz = t[1]
    except IndexError as e:
        print(e)
        print('Falsche Positions Angabe')
    x = TISCHE[raum][tisch][0] + PLATZ[raum][platz][0]
    y = TISCHE[raum][tisch][1] + PLATZ[raum][platz][1]
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
    kurs = ''
    fach = ''
    raum = ''

    def __init__(self, kurs='', fach='', raum='', kursDatei=''):
        #global DATUM
        self.kurs = kurs
        self.fach = fach
        self.raum = raum
        self.klassenDatei = dict()
        try:
            with open(kursDatei, 'r') as f:
                self.klassenDatei = json.load(f)
        except Exception as e:
            print('something went wrong')
            print('habe keine klassen-datei geladen')
            print(kursDatei)
            print(e)
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
        #testweise: später als key in dict
        self.kursOptions = list(self.klassenDatei.keys())
        self.kursOptions.append('...')
        self.ausgewaehlterKurs = StringVar()
        self.ausgewaehlterKurs.set(self.kursOptions[0])
        self.klasseAuswaehlen = OptionMenu(self.fenster, self.ausgewaehlterKurs, *self.kursOptions)
        self.klasseAuswaehlen.place(x=700, y=10, width=120)
        self.klasseLaden = Button(self.fenster, text='Klasse laden', command=self.ladeKlasse)
        self.klasseLaden.place(x=700, y=50, width=120)
        self.speichern = Button(self.fenster, text='speichern', command=self.speicherKlasse)
        self.speichern.place(x=700, y=90, width=120)
        self.speichern.config(state=tkinter.DISABLED)
        self.klasseBearbeiten = Button(self.fenster, text='Klasse bearbeiten', command=self.klasse_bearbeiten)
        self.klasseBearbeiten.place(x=700, y=130, width=120)
        self.klasseBearbeiten.config(state=tkinter.DISABLED)
        self.thema = Label(self.fenster, text='Thema der Stunde')
        self.thema.place(x=700, y=170, width=120)
        self.benutzer = Entry(self.fenster)  # Kaffeetasse show=u'\u2615'
        # self.passwort = Entry(self.fenster)  # Atom show=u'\u269B'
        self.benutzer.place(x=700, y=210, width=120)
        self.benutzer.config(state=tkinter.DISABLED)
        self.einzelStunde = Button(self.fenster, text='Einzelstunde', command=self.einzelDoppel)
        self.einzelStunde.place(x=700, y=250, width=120)
        self.einzelStunde.config(state=tkinter.DISABLED)
        self.mitarbeitGut = Button(self.fenster, text='+', command=self.bewertenPlus)
        self.mitarbeitGut.place(x=700, y=290, width=30)
        self.mitarbeitGut.config(state=tkinter.DISABLED)
        self.mitarbeitMittel = Button(self.fenster, text='o', command=self.bewertenKreis)
        self.mitarbeitMittel.place(x=740, y=290, width=30)
        self.mitarbeitMittel.config(state=tkinter.DISABLED)
        self.mitarbeitSchlecht = Button(self.fenster, text='-', command=self.bewertenMinus)
        self.mitarbeitSchlecht.place(x=780, y=290, width=30)
        self.mitarbeitSchlecht.config(state=tkinter.DISABLED)
        self.keineHausaufgaben = Button(self.fenster, text='keine HA', command=self.keineHA)
        self.keineHausaufgaben.place(x=700, y=330, width=120)
        self.keineHausaufgaben.config(state=tkinter.DISABLED)
        self.abwesendBtn = Button(self.fenster, text='nicht da', command=self.abwesend)
        self.abwesendBtn.place(x=700, y=370, width=120)
        self.abwesendBtn.config(state=tkinter.DISABLED)
        self.platztauschenBtn = Button(self.fenster, text='Platz tauschen', command=self.platzTauschen)
        self.platztauschenBtn.place(x=700, y=410, width=120)
        self.platztauschenBtn.config(state=DISABLED)
        self.datumBtn = Button(self.fenster, text=DATUM, command=self.datumAendern)
        self.datumBtn.place(x=700, y=450, width=120)
        self.datumBtn.config(state=tkinter.DISABLED)
        #sus einlesen
        self.setzeSuS(neu=True)

    def setzeSuS(self, neu):
        if neu:
            try:
                for key in self.all:
                    self.all[key].button.destroy()
            except Exception as e:
                print(e)
                print('es gibt vermutlich noch keine klasse')
        self.all = dict()
        if self.raum in RAEUME:
            id = 0
            nTische = len(TISCHE[self.raum].keys())
            nPlaetze = len(PLATZ[self.raum])
            for i in range(1, nTische+1):
                for j in range(1, nPlaetze+1):
                    id += 1
                    self.all[id] = SuS(id=id,
                                            name=str(id),
                                            stufe='8',
                                            raum=self.raum,
                                            pos=(i, j),
                                            fenster=self.fenster)

    def bewerten(self, n):
        print(n)
        self.mitarbeitGut['state'] = tkinter.NORMAL
        self.mitarbeitMittel['state'] = tkinter.NORMAL
        self.mitarbeitSchlecht['state'] = tkinter.NORMAL

    def bewertenPlus(self):
        global AKTIVESUS
        for id in AKTIVESUS:
            self.all[id].benoten(note=1, thema=self.benutzer.get()) # test stundenthema
            nameTemp = self.all[id].name + ' +'
            self.all[id].button.configure(text=nameTemp, bg='green')
            self.all[id].isActive = not self.all[id].isActive
        AKTIVESUS.clear()

    def bewertenKreis(self):
        global AKTIVESUS
        for id in AKTIVESUS:
            self.all[id].benoten(note=0, thema=self.benutzer.get())
            nameTemp = self.all[id].name + ' o'
            self.all[id].button.configure(text=nameTemp, bg='orange')
            self.all[id].isActive = not self.all[id].isActive
        AKTIVESUS.clear()

    def bewertenMinus(self):
        global AKTIVESUS
        for id in AKTIVESUS:
            self.all[id].benoten(note=-1, thema=self.benutzer.get())
            nameTemp = self.all[id].name + ' -'
            self.all[id].button.configure(text=nameTemp, bg='red')
            self.all[id].isActive = not self.all[id].isActive
        AKTIVESUS.clear()

    def keineHA(self):
        global AKTIVESUS
        for id in AKTIVESUS:
            self.all[id].keineHA()
            self.all[id].button.configure(bg='magenta') #deeppink1
            self.all[id].isActive = False
        AKTIVESUS.clear()
        pass


    def abwesend(self):
        global  AKTIVESUS
        for id in AKTIVESUS:
            self.all[id].abwesend()
            self.all[id].button.configure(bg='blue')
            self.all[id].isActive = False
        AKTIVESUS.clear()

    def ladeKlasse(self):
        global STATUS
        dictTemp = dict()
        if ALLDATAINONE:
            aktiverkurs = self.ausgewaehlterKurs.get()
            if aktiverkurs == '...':
                self.klasse_bearbeiten()
            self.fenster.title(aktiverkurs)
            dictTemp = self.klassenDatei[aktiverkurs]
        else:
            filePfad = filedialog.askopenfilename(initialdir='D:/03_Noten')
            with open(filePfad, 'r') as f:
                dictTemp = json.load(f)
            self.fenster.title(dictTemp['0']['Klasse'] + ' - ' + dictTemp['0']['Fach'])
        for key in dictTemp:
            key = int(key)
            if key == 0:
                try:
                    self.kurs = dictTemp[key]['Klasse']
                    self.fach = dictTemp[key]['Fach']
                    self.raum = dictTemp[key]['Raum']
                except KeyError as ke:
                    self.kurs = dictTemp[str(key)]['Klasse']
                    self.fach = dictTemp[str(key)]['Fach']
                    self.raum = dictTemp[str(key)]['Raum']
                self.setzeSuS(neu=True)
            else:
                try:
                    self.all[key].loadOldDict(dictTemp[key])
                except KeyError as ke:
                    self.all[key].loadOldDict(dictTemp[str(key)])
        self.speichern.config(state=tkinter.NORMAL)
        self.klasseBearbeiten.config(state=tkinter.NORMAL)
        self.benutzer.config(state=tkinter.NORMAL)
        self.einzelStunde.config(state=tkinter.NORMAL)
        self.mitarbeitGut.config(state=tkinter.NORMAL)
        self.mitarbeitMittel.config(state=tkinter.NORMAL)
        self.mitarbeitSchlecht.config(state=tkinter.NORMAL)
        self.keineHausaufgaben.config(state=tkinter.NORMAL)
        self.abwesendBtn.config(state=tkinter.NORMAL)
        self.platztauschenBtn.config(state=tkinter.NORMAL)
        self.datumBtn.config(state=tkinter.NORMAL)
        print(dictTemp)


    def klasse_bearbeiten(self):
        global STATUS
        if STATUS != STATI['Klasse erstellen']:
            STATUS = STATI['Klasse erstellen']
            if self.ausgewaehlterKurs.get() == '...':
                klassenInfos = getInfosForKlasse(self.fenster)
                klassenInfos.okayButton.wait_window(klassenInfos.popUp)
                klassenName = KURSNAME
                self.kurs = klassenName.split('-')[0]
                self.fach = klassenName.split('-')[1]
                self.raum = klassenName.split('-')[2]
                self.setzeSuS(neu=True)
            else:
                pass
                #self.setzeSuS(neu=False)
            self.klasseBearbeiten.configure(text='Bearbeiten Beenden')
            self.fenster.title('Klasse erstellen')
        else:
            STATUS = STATI['neutral']
            self.klasseBearbeiten.configure(text='Klasse bearbeiten')
            self.fenster.title(KURSNAME)
            self.speicherKlasse()
            self.klasseAuswaehlen['menu'].delete(1, 'end')
            for key in self.klassenDatei:
                self.klasseAuswaehlen['menu'].add_command(label=key, command=lambda value=key: self.ausgewaehlterKurs.set(value))

    def speicherKlasse(self):
        global SPEICHERNAME
        fileDir = 'D:/03_Noten/'
        dictToSave = dict()
        kursName = self.kurs + '-' + self.fach + '-' + self.raum
        print(kursName)
        dictToSave[0] = {
            'Klasse': self.kurs,
            'Fach': self.fach,
            'Raum': self.raum
        }
        for id in self.all:
            dictTemp = copy.copy(self.all[id].makeDictForSave())
            dictToSave[id] = dictTemp
        if ALLDATAINONE:
            self.klassenDatei[kursName] = dictToSave
            with open(SPEICHERNAME, 'w') as f:
                json.dump(self.klassenDatei, f, indent=2)
        else:
            filename = self.kurs + '-' + self.fach
            with open(fileDir + filename, 'w') as f:
                json.dump(dictToSave, f, indent=2)
        self.ladeKlasse()

    def einzelDoppel(self):
        #TODO: individuelle Gewichtung -> Test also 5/45
        #TODO: Klassenarbeiten (Benotung)
        #TODO: Heft mit E- und G-Kurs gewichtung
        global STUNDENZAHL
        if self.einzelStunde['text'] == 'Einzelstunde':
            self.einzelStunde['text'] = 'Doppelstunde'
            STUNDENZAHL = 2
            print(STUNDENZAHL)
        else:
            self.einzelStunde['text'] = 'Einzelstunde'
            STUNDENZAHL = 1
            print(STUNDENZAHL)

    def platzTauschen(self):
        global AKTIVESUS
        if len(AKTIVESUS) == 2:
            ids = list()
            for id in AKTIVESUS:
                ids.append(id)
            idA = ids[0]
            idB = ids[1]
            susB = self.all[idB]
            self.all[idB] = self.all[idA]
            self.all[idA] = susB
        AKTIVESUS.clear()
        self.speicherKlasse()
        self.ladeKlasse()

    def datumAendern(self):
        global DATUM
        d = getDatum(self.fenster)
        d.okayButton.wait_window(d.popUp)
        self.datumBtn.configure(text=DATUM)



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
    keineHausaufgaben = set()

    def __init__(self, id, name, stufe, raum, pos, muendlichBool=True, bild='', fenster=''):
        # stufe: 5 bis 13
        # bild: Pfad zur Datei
        global B, H
        self.id = id
        self.name = name
        self.stufe = stufe
        self.raum = raum
        self.platz = dict()
        self.platz[self.raum] = pos
        self.muendlichBool = muendlichBool
        self.bild = bild
        self.benotungsDict = dict()
        self.button = Button(fenster, text=name, wraplength=50)
        self.button.place(x=getPos(self.platz[self.raum], raum=self.raum)[0],
                          y=getPos(self.platz[self.raum], raum=self.raum)[1], width=B, height=H)
        self.button.configure(command=self.doStuff)
        self.fenster = fenster

    def loadOldDict(self, oldDict):
        self.name = oldDict['Name']
        self.stufe = oldDict['Stufe']
        self.raum = oldDict['Raum']
        self.platz = oldDict['Platz']
        self.muendlichBool = oldDict['MuendlichBool']
        self.bild = oldDict['Bild']
        self.benotungsDict = oldDict['Benotung']
        self.button['text'] = self.name
        self.keineHausaufgaben = set(oldDict['Hausaufgaben'])
        pass

    def doStuff(self):
        global AKTIVESUS, GESAMTNAME
        print(self.isActive)
        self.isActive = not self.isActive
        if self.isActive:
            self.button.configure(bg='yellow')
            AKTIVESUS.add(self.id)
            if STATUS == STATI['Klasse erstellen'] or STATUS == STATI['Klasse bearbeiten']:
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
        self.button.place(x=getPos(self.platz[self.raum], raum=self.raum)[0],
                          y=getPos(self.platz[self.raum], raum=self.raum)[1], width=60, height=90)

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
        self.dictForSave['Hausaufgaben'] = list(self.keineHausaufgaben)
        return self.dictForSave

    def benoten(self, note, kommentar='', thema=''):
        global STUNDENZAHL, DATUM
        #print(STUNDENZAHL)
        tag = str(DATUM)
        self.benotungsDict[tag] = (note, STUNDENZAHL, kommentar, thema)
        pass

    def keineHA(self):
        tag = str(datetime.datetime.now().date())
        self.keineHausaufgaben.add(tag)

    def abwesend(self):
        tag = str(datetime.datetime.now().date())
        self.benotungsDict[tag] = (0, 0, 'nicht da')


if __name__ == '__main__':
    SPEICHERNAME
    if len(sys.argv) == 2:
        SPEICHERNAME = str(sys.argv[1])
        vk = VirtuellerKlassenraum(kursDatei=SPEICHERNAME)
        #vk = VirtuellerKlassenraum()
        vk.fenster.mainloop()
    else:
        print('keine Inputdatei')
        print('nutze:')
        print('python main.py speicherort')
        exit(1)
