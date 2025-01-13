len_of_numbers = int(input())

list_of_outputs = []

for i in range(len_of_numbers):
    try:
        a, b = map(int, input().split())
        list_of_outputs.append(a//b)
    except ZeroDivisionError:
        list_of_outputs.append('Error Code: integer division or modulo by zero')
    except ValueError as e:
        list_of_outputs.append("Error Code: " + str(e))

[print(x) for x in list_of_outputs]
