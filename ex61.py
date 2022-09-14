print("-"*30)
print('PROGRESSÕES ARITMÉTICAS')
print("-"*30)
p=int(input('Qual o primeiro termo da sua PA: '))
r=int(input('Qual a razão da sua PA: '))
print("-"*30)
t=10
cont=0
lis=[]
cont1=1
while cont<t:
    pa=p+(cont*r)
    cont=cont+1
    lis.append(pa)
    print(f'{pa}->', end='')
print('PAUSE')
print("-"*30)
while True:
    ct=str(input('Deseja continunar:[S/N]')).upper().strip()[0]
    print("-" * 30)
    if ct=='N':
        print('FIM DO PROGRAMA')
        break
    elif ct=="S":
        ct2=int(input('Quantos termos você quer montrar a mais:'))
        for i in range(0,ct2):
            n=len(lis)
            pa1 = lis[n-1] + (cont1 * r)
            lis.append(pa1)
            print(f'{pa1}->', end='')
        print('PAUSE')
print("-"*30)
print(f'O número de termos final da PA é {len(lis)}!')





