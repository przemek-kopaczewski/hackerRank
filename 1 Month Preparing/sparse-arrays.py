#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    numbers_of_reply = []
    for query in queries:
        reply = 0
        for word in strings:
            if query == word:
                reply+=1

        numbers_of_reply.append(reply)

    for row in numbers_of_reply:
        print(row)

strings_count = int(input().strip())

strings = []

for _ in range(strings_count):
    strings_item = input()
    strings.append(strings_item)

queries_count = int(input().strip())

queries = []

for _ in range(queries_count):
    queries_item = input()
    queries.append(queries_item)

matchingStrings(strings, queries)
