def nb_repetitions(elt,tab):
    nb=0
    for element in tab:
        if element==elt:
            nb+=1
    return nb


print(nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]))
print(nb_repetitions('A', ['B', 'A', 'B', 'A', 'R']))
print(nb_repetitions(12, [1, 3, 7, 21, 36, 44]))