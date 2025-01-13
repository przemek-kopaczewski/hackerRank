tab = [93,21,30,80,100,28,9,70,47,18,9,66,29,11,37]

for i in range(len(tab)):
    j = i - 1
    pom = tab[i]
    while j >= 0 and tab[j] > pom:
        tab[j+1] = tab[j]
        j-=1
    tab[j+1] = pom

print(tab)