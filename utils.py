B = 60  # Bild/Button-Breite
H = 90  # Bild/Button-Höhe

RAEUME = ['54', '48', '49a', 'A', 'C', 'D']

TISCHE = {
    '54': {  # Physikraum 54
        1: (10, 10),  # hinten links
        2: (int(2 * (B + 10) + 1 * 40), 10),  # hinten rechts
        3: (int(4 * (B + 10) + 2 * 40), 10),  # vorne links
        4: (int(6 * (B + 10) + 3 * 40), 10),  # vorne rechts
    },
    '49a': {  # Chemieraum 49a
        1: (10, 10),                                            # hinten links
        2: (int(4 * (B + 10) + 2 * 40), 10),                    # hinten rechts
        3: (int(2 * (B + 10) + 40), int(10 + 2 * (H + 10))),    # vorne links
        4: (int(6 * (B + 10) + 3 * 40), int(10 + 2 * (H + 10))) # vorne rechts
    }
}
PLATZ = {
    '8': {
        1: (int(0 * (B + 10)), int(0 * (H + 10))),
        2: (int(1 * (B + 10)), int(0 * (H + 10))),
        3: (int(0 * (B + 10)), int(1 * (H + 10))),
        4: (int(1 * (B + 10)), int(1 * (H + 10))),
        5: (int(0 * (B + 10)), int(2 * (H + 10))),
        6: (int(1 * (B + 10)), int(2 * (H + 10))),
        7: (int(0 * (B + 10)), int(3 * (H + 10))),
        8: (int(1 * (B + 10)), int(3 * (H + 10)))
    }
}
STATI = {
    'neutral': 0,
    'Klasse erstellen': 1,
    'Klasse bearbeiten': 2,
    'SuS bearbeiten': 3
}

def getPos(t, raum='54', anordnung='8'):
    try:
        tisch = t[0]
        platz = t[1]
    except IndexError as e:
        print(e)
        print('Falsche Positions Angabe')
    x = TISCHE[raum][tisch][0] + PLATZ[anordnung][platz][0]
    y = TISCHE[raum][tisch][1] + PLATZ[anordnung][platz][1]
    return (x, y)