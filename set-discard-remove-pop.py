a = input()
zbior = set(map(int, input().split()))

for i in range(int(input())):
    action = input()
    action = action.split()
    if action[0] == 'remove':
        exec(f'zbior.{action[0]}({action[1]})')
    elif action[0] == 'discard':
        exec(f'zbior.{action[0]}({action[1]})')
    elif action[0] == 'pop':
        exec(f'zbior.{''.join(action)}()')


print(sum(zbior))