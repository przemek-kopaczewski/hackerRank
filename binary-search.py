search_number = int(input())
list_of_numbers = list(map(int, input().rstrip().split()))
list_of_numbers = sorted(list_of_numbers)
find = False
L, P = 0, len(list_of_numbers)-1
S = (L + P) / 2
while find is False:
    if list_of_numbers[int(S)] == search_number:
        print(int(S))
        find = True
    elif list_of_numbers[int(S)] < search_number:
        L = S + 1
        S = (L + P) / 2
    elif list_of_numbers[int(S)] > search_number:
        P = S - 1
        S = (L + P) / 2