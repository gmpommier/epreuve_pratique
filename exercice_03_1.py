def maximum_tableau(tab):
    maximum = tab[0]
    for element in tab:
        if element > maximum:
            maximum = element
    return maximum

print(maximum_tableau([98, 12, 104, 23, 131, 9]))

print(maximum_tableau([-27, 24, -3, 15]))
