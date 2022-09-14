import random
lista=[]
cont=0
for i in range(0,5):
    t=random.randint(0,100)
    lista.append(t)
    cont=cont+1
print(lista)
n=min(lista)
print(n)
n1=max(lista)
print(n1)
