import os
import json
import sys

if len(sys.argv) == 2:
    pfad = sys.argv[1]
else:
    print('keine Notendatei')
    print('nutze:')
    print('python readNoten.py speicherort')
    exit(1)

with open(pfad, 'r') as f:
    klassenDatei = json.load(f)

kurse = list(klassenDatei.keys())

EXIT = False


def printNotenliste(nKurs):
    aktiverKurs = klassenDatei[kurse[nKurs]]
    for sus in aktiverKurs:
        if sus == '0':
            print(aktiverKurs[sus])
        else:
            gutmittelschlechtSumme = 0
            nStunden = 0
            name = aktiverKurs[sus]['Name'].split(' ')
            try:
                printLine = name[0] + ' ' + name[1]
            except IndexError:
                printLine = name[0]
            try:
                if not bool(printLine.strip()):
                    printLine=0
                dump = int(printLine)
            except ValueError:
                for day in aktiverKurs[sus]['Benotung']:
                    gutmittelschlechtSumme += aktiverKurs[sus]['Benotung'][day][0] * aktiverKurs[sus]['Benotung'][day][1]
                    nStunden += aktiverKurs[sus]['Benotung'][day][1]
                try:
                    rawPunkte = gutmittelschlechtSumme/nStunden
                    if rawPunkte <= 0:
                        note = -2 * rawPunkte + 4
                        punkte = 5 * rawPunkte + 5
                    else:
                        note = -3 * rawPunkte + 4
                        punkte = 10 * rawPunkte + 5
                    while len(printLine) <= 20:
                        printLine += ' '
                    printLine += 'Note: ' + str(round(note, 2)).replace('.', ',')
                    while len(printLine) <= 35:
                        printLine += ' '
                    printLine += 'Puntke: ' + str(round(punkte, 1)).replace('.', ',')
                    while len(printLine) <= 50:
                        printLine += ' '
                    printLine += 'Stunden anwesend: ' + str(nStunden)
                except ZeroDivisionError:
                    printLine += ' war 0 Stunden da'
                finally:
                    print(printLine)


def printKursliste():
    kurse = list(klassenDatei.keys())
    n = 0
    for kurs in kurse:
        print(str(n) + '____' + kurs)
        n += 1


def printSuS():
    pass

def mainloop():
    global EXIT
    printKursliste()
    try:
        eingabe = input('Wähle einen Kurs, oder [q], [x], [exit] zum schließen:\n')
        exitWords = ['x', 'q', 'exit']
        if eingabe in exitWords:
            print('Auf wiedersehn')
            EXIT = True
        else:
            nK = int(eingabe)
            printNotenliste(nK)


    except ValueError:
        print('Input muss die dem Kurs entsprechende Zahl sein')


if __name__ == '__main__':
    while not EXIT:
        mainloop()
        eingabe = input('Drücke Enter für einen weiteren kurs oder [q], [x], [exit] zum verlassen.\n')
        if eingabe in ['q', 'x', 'exit']:
            print('Auf wiedersehn!')
            EXIT = True