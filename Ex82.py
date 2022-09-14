l=[]
lp=[]
li=[]

while True:
    n=int(input('Digite um Número:'))
    l.append(n)
    if n%2==0:
        lp.append(n)
    else:
        li.append(n)
    k = str(input('Deseja continuar:(S/N)')).strip().upper()
    if k=='N':
        break
print(l)
print(lp)
print(li)

