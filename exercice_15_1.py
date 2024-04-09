def moyenne(tab):
    somme=0
    for i in tab:
        somme+=i
    return somme/len(tab)





print(moyenne([1.0]))
print(moyenne([1.0, 2.0, 4.0]))