def recherche_indices_classement(elt, tab):
    ind_inf = []
    ind_egal = []
    ind_sup = []
    for i in range(len(tab)):
        if tab[i] < elt:
            ind_inf.append(i)
        elif tab[i] > elt:
            ind_sup.append(i)
        else:
            ind_egal.append(i)
    return (ind_inf, ind_egal, ind_sup)

print(recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0]))
print(recherche_indices_classement(3, [1, 4, 2, 4, 6, 0]))
print(recherche_indices_classement(3, [1, 1, 1, 1]))
print(recherche_indices_classement(3, []))
