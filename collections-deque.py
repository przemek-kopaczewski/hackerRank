from collections import deque

zbior = deque()

for i in range(int(input())):
    action = input()
    action = action.split()
    if len(action) == 2:
        exec(f'zbior.{action[0]}({action[1]})')
    else:
        exec(f'zbior.{''.join(action)}()')

zbior = list(map(str, zbior))
print(' '.join(zbior))