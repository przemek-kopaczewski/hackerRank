for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    #print(''.join(f'{j}' for j in range(1, i + 1))+''.join(f'{j}' for j in range(i-1, 0, -1)))
    print((10 ** i // 9) ** 2)