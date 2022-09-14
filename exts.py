import time

produtos=["arroz", "macarrão", "feijão", "cebola", "tomate"]
valor=[10,7,10,4,6]
vendas=[1200,300,800,150,1900,2750,20, 950, 100, 1000, 2000, 1500, 300, 500, 800]


"""tamanho=len(vendas)
print(tamanho)
cont=0
for i in range(tamanho):
    if vendas[i]>=meta:
       cont=cont+1
p=float(cont*100)/tamanho
print(f"{p}% atingiram a meta.")"""

'''fb=int(input('Digite um número: '))
lista=[1,1]
cont=2
f=0
while True:
    time.sleep(0.5)
    if cont>=2:
        f=lista[cont-1]+lista[cont-2]
        lista.append(f)
        cont = cont + 1
    if cont==fb:
        break
print(lista)'''
'''for i,v in enumerate(produtos):
    print(f'{i} -> {v}')'''

n=int(input('Digite um número: '))
for i in range(1,11):
    print(f'{n} x {i} = {n*i}')
