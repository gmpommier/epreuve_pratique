def gb_vers_entier(tab):
    somme = 0
    for i in range(len(tab)):
        if tab[i]:
            somme += 2**(len(tab)-1-i)
    return somme

print(gb_vers_entier([]))
print(gb_vers_entier([True]))
print(gb_vers_entier([True, False, True, False, False, True, True]))
print(gb_vers_entier([True, False, False, False, False, False, True, False]))
