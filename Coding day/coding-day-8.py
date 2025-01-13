length = int(input())
phone_book = {tuple(input().split()) for i in range(length)}

phone_book = dict(phone_book)
pom = True

try:
    while pom:
        input_name = input()
        if input_name in phone_book:
            print('{}={}'.format(input_name, phone_book[input_name]))
        else:
            print('Not found')
except:
    pom = False
