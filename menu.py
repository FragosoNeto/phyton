import math
import numpy
n1 = int(input('Digite o primeiro número?'))
n2 = int(input('Digite o segundo número?'))
y=0
while y != 5:
    print('MENU')
    x1 = print('[1] SOMA')
    x2 = print('[2] MULTIPLICAR')
    x3 = print('[3] MAIOR')
    x4 = print('[4] NOVOS NÚMEROS')
    x5 = print('[5] SAIR DO PROGRAMA')
    y1 = int(input('QUAL A SUA OPÇÃO:'))
    y=y+y1
    if y1==1:
        s=n1+n2
        print(s)
    elif y1==2:
        m=n1*n2
        print(m)
    elif y1==3:
        k=max(n1,n2)
        print(k)
    elif y1==4:
        n1 = int(input('Digite o primeiro número?'))
        n2 = int(input('Digite o segundo número?'))
    elif y1!=1 and y1!=2 and y1!=3 and y1!=4 and y1!=5:
        print('NÚMERO INVÁLIDO. TENTE NOVAMENTE')

print('FIM')






