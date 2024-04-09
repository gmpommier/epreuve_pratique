def min_et_max(tab):
    d = {}
    d['min'] = tab[0]
    d['max'] = tab[0]
    for val in tab:
        if val < d['min']:
            d['min'] = val
        if val > d['max']:
            d['max'] = val
    return d

print(min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]))
print(min_et_max([0, 1, 2, 3]))
print(min_et_max([3]))
print(min_et_max([1, 3, 2, 1, 3]))
print(min_et_max([-1, -1, -1, -1, -1]))