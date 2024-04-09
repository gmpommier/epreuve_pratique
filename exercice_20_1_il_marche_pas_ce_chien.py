from random import randint

def lancer(n):
    return [randint(1, 6) for _ in range(n)]

def paire_6(tab):
    nb = 0
    for elt in tab:
        if elt == 6:
            nb += 1
    if nb >= 2 :
        return True
    else:
        return False

lancer1 = lancer(5)
print(paire_6(lancer1))
print(lancer2 = lancer(5))
print(paire_6(lancer2))
print(lancer3 = lancer(3))
print(paire_6(lancer3))
print(lancer4 = lancer(0))
print(paire_6(lancer4))
