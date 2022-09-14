import random
def ct():
    list=[]
    listp=[]
    cont=0
    while True:
        cont=cont+1
        n=random.randint(1,100)
        list.append(n)
        if n%2==0:
            listp.append(n)
        if cont==10:
            print(f'Foram soteados 10 valores:{list} PRONTO!')
            print(f'Os valores pares são:{listp}')
            print(f'A soma dos valores pares é {sum(listp)}!')
            break

ct()
