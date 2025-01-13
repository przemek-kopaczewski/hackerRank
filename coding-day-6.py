for i in range(int(input())):
    string = input()
    string_even = ''
    string_odd = ''
    for j in range(len(string)):
        if j == 0 or j % 2 == 0:
            string_even+=string[j]
        else:
            string_odd+=string[j]
    print('{} {}'.format(string_even, string_odd))