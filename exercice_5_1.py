def max_et_indice(tab):

    val_max = tab[0]
    ind_max = 0
    for i in range(len(tab)):
        if tab[i] > val_max:
            val_max = tab[i]
            ind_max = i
    return (val_max, ind_max)

print(max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
print(max_et_indice([-2]))
print(max_et_indice([-1, -1, 3, 3, 3]))
print(max_et_indice([1, 1, 1, 1]))
