def multiplication(n1, n2):
    if n1 < 0:
        return -multiplication(-n1, n2)
    if n2 < 0:
        return -multiplication(n1, -n2)
    resultat = 0
    for _ in range(n2):
        resultat += n1
    return resultat




print(multiplication(3,5))
print(multiplication(-4,-8))
print(multiplication(-2,6))
print(multiplication(-2,0))
