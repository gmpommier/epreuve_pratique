def depouille(urne):
    '''prend en paramètre une liste de suffrages et renvoie un
    dictionnaire avec le nombre de voix pour chaque candidat'''
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueurs(election):
    '''prend en paramètre un dictionnaire non vide avec le nombre de voix
    pour chaque candidat et renvoie la liste des vainqueurs'''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax:
            nmax = election[candidat]
    liste_finale = [ nom for nom in election if election[nom] == nmax ]
    return liste_finale



print(depouille([ 'A', 'B', 'A' ]))
print(depouille([]))
print(election = depouille(['A', 'A', 'A', 'B', 'C','B', 'C', 'B', 'C', 'B']))
print(vainqueurs(election)
printvainqueurs({ 'A' : 2, 'B' : 2, 'C' : 1})
