from collections import defaultdict

dict_of_food = defaultdict(list)

for i in range(int(input())):
    values = list(map(str, input().split()))
    if values[0] and values[1].isalpha():
        item_name  = values[0] + " " + values[1]
        dict_of_food[item_name].append(int(values[2]))
    else:
        item_name = values[0]
        dict_of_food[item_name].append(int(values[1]))

for key, values in dict_of_food.items():
    dict_of_food[key] = sum(values)

for key, value in dict_of_food.items():
    print(key, value)