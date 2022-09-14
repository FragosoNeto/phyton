cont=0
l=[]
for i in range(0,5):
    n=int(input(f'Digite o promeiro número na posição {cont}:'))
    cont=cont+1
    n1=l.append(n)
print(f'Você digitou os valores:{l}')
n2=max(l)
n3=min(l)
for a1,v in enumerate(l):
    if v==n2:
        print(f'O maior número está na posição {a1} e é {n2}')
for a2,v in enumerate(l):
    if v==n3:
        print(f'O menor número está na posição {a2} e é {n3}')