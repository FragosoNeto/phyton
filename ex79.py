l=[]
t='SN'
while True:
    n=int(input('Digite um número:'))
    a=l.append(n)
    c=l.count(n)
    if c==2:
        l.remove(n)
        print('Número repetido')
        t = str(input('Deseja continuar:(S/N)')).strip().upper()[0]
        if t == 'N'.upper():
            break
    elif c==1:
        print('Valor adicionado com sucesso')
        t = str(input('Deseja continuar:(S/N)')).strip().upper()[0]
        if t == 'N'.upper():
            break
l.sort()
print(l)



