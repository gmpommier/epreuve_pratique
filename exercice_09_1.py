# Créé par gabriel.pommier, le 02/04/2024 en Python 3.7
def effectif_notes(notes_eval):
    tab = [0]*11
    for note in notes_eval:
        tab[note] += 1
    return tab

def notes_triees(eff):
    triees = []
    for i in range(11):
        if eff[i] != 0:
            for _ in range(eff[i]):
                triees.append(i)
    return triees
