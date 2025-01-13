tab = [93,21,30,80,100,28,9,70,47,18,9,66,29,11,37]
#Napisz funkcję lambda, która przyjmuje jedną liczbę i zwraca jej kwadrat.
print((lambda x: x**2)(2))

#Napisz funkcję lambda, która przyjmuje dwa argumenty (a i b) i zwraca ich sumę.
print((lambda x, y: x + y)(3,7))

#Użyj funkcji lambda z funkcją map, aby podnieść każdą liczbę w liście do kwadratu.
print(list(map(lambda x: x**2, tab)))

#Użyj funkcji lambda z funkcją filter, aby wybrać z listy tylko liczby parzyste.
print(list(filter(lambda x: x%2==0, tab)))

tupla = [(45, 67), (23, 89), (34, 12), (56, 78), (90, 34), (12, 56), (78, 23), (45, 90)]
#Mając listę tupli, gdzie każda tupla zawiera dwie liczby, posortuj tę listę według drugiej liczby w
#każdej tupli, używając funkcji lambda.
tupla.sort(key=lambda x: x[1])
print(tupla)

#Użyj funkcji lambda do sortowania listy słowników według wartości przypisanej do konkretnego klucza.
people = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 23}]
people.sort(key=lambda x: x['age'])
print(people)

#Napisz funkcję lambda, która zwraca True, jeśli dana liczba jest liczbą pierwszą, w przeciwnym razie False.
print(lambda x: )