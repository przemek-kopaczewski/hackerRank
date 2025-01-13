tab = [93,21,30,80,100,28,9,70,47,18,9,66,29,11,37]

for i in range(len(tab)):
    for j in range(len(tab)):
        if tab[j] > tab[i]:
            tab[i], tab[j] = tab[j], tab[i]
print(tab)