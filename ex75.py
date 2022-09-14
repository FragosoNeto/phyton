t=(int(input('Informe um número')),int(input('Informe um número')),int(input('Informe um número')),int(input('Informe um número')),int(input('Informe um número')))
np=[]
cont=0
for n in t:
    if n%2==0:
        np.append(n)
        cont=cont+1
    print(n)
t1=t
n1=max(t)
n2=min(t)
n3=t.count(9)
n4=t1.index(3)
print('-'*30)
print(n1)
print('-'*30)
print(n2)
print('-'*30)
print(n3)
print('-'*30)
print(n4)
print('-'*30)
print(np)
