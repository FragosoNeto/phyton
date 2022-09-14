import random
c=0
while True:
    print('=-'*30)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=-' * 30)
    n=int(input('DIGITE UM NÚMERO:'))
    op=str(input('PAR OU ÍMPAR(P/I):')).upper().strip()[0]
    c=random.randint(0,10)
    r=(n+c)%2
    if r==0 and op=='P':
        print('VOCÊ VENCEU')
        c = c + 1
    elif r!=0 and op=="I":
        print('VOCÊ VENCEU')
        c = c + 1
    else:
        break
print(f'VOCÊ JOGOU {c} PARTIDAS')
print('VOCÊ PERDEU')
print('FIM')






