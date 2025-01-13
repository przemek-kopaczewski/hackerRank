import re


regex = r'^[4-6](?!.*([0-9])\1{3,}).{15}$'

ilosc = int(input())

for repeat in range(ilosc):
    credit_card = input()
    if '-' in credit_card:
        credit_card = credit_card.split('-')
        check_4 = all(len(numbers) == 4 for numbers in credit_card)
        if check_4 is True:
            credit_card = ''.join(credit_card)
            if bool(re.fullmatch(regex, credit_card)):
                print('Valid')
            else:
                print('Invalid')
        else:
            print('Invalid')
    else:
        if bool(re.fullmatch(regex, credit_card)):
            print('Valid')
        else:
            print('Invalid')