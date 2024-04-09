def verifie(tab):
    for i in range(1, len(tab)):
        if tab[i] < tab[i-1]:
            return False
    return True

print(verifie([0, 5, 8, 8, 9]))
print(verifie([8, 12, 4]))
print(verifie([-1, 4]))
print(verifie([]))
print(verifie([5]))
