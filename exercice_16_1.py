def ecriture_binaire_entier_positif(n):
    if n==0:
        return '0'
    binaire=''
    while n!=0:
        binaire=str(n%2)+binaire
        n= n//2
    return binaire

print(5 % 2)
print(5 // 2)
print(ecriture_binaire_entier_positif(0))
print(ecriture_binaire_entier_positif(2))
print(ecriture_binaire_entier_positif(105))
