import string
#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    alphabet = string.ascii_lowercase
    word = set(s.lower().replace(' ', ''))
    word = ''.join(sorted(list(word)))
    if word == alphabet:
        return 'pangram'
    else:
        return 'not pangram'


s = input()
print(pangrams(s))