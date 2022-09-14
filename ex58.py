import random

print('Sou seu computador!')
print('Acabei de pensar em um número de 0 a 10!')
n=random.randint(0,10)
print('Qual é o seu palpite?')
cont=0
while True:
    x=int(input('Digite um número: '))
    if x==n:
        print('Você Ganhou')
        break
    elif x>n:
        print('Menos....Tente mais uma vez!')
    elif x<n:
        print('Mais....Tente mais uma vez!')
    cont=cont+1
print(f'Você conseguiu em {cont+1} tentativas')
