while True:
    n = int(input('Digite um número para o cáculo da respectiva taboada:'))
    if n>0:
        for c in range(1, 11):
            t = c * n
            print(n,'x',c,'=',t)
    else:
        break
print('término da taboada')



