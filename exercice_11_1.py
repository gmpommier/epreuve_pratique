# Créé par gabriel.pommier, le 02/04/2024 en Python 3.7
def nombre_de_mots(phrase):
    nb_mots = 0
    for caractere in phrase:
        if caractere == ' ' or caractere == '.':
            nb_mots += 1
    return nb_mots
