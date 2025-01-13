from collections import OrderedDict
def merge_the_tools(string, k):
    result = [string[char:char+k] for char in range(0, len(string), k)]
    final = []
    for word in result:
        final.append("".join(OrderedDict.fromkeys(word)))
    for word in final:
        print(word)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)