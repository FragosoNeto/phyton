n=float(input('Valor total das compras:'))
a=print('1-Pagamento à vista(10% de desconto):')
b=print('2-Pagamento à vista no Cartão(5% de desconto):')
c=print('3-Pagamento no cartão em até 2 vezes(preço normal):')
d=print('4-Pagamento no cartão em 3 ou mais vezes(juros de 20%):')
n1=int(input('Escolha uma das opções:'))
if n1==1:
    a1 = n - (n * 0.1)
    print(a1)
elif n1 == 2:
    b1=n-(n*0.05)
    print(b1)
else:
    n2=int(input('Quantas parcelas?'))
if n1==3:
    print(n / n2)
elif n1==4:
    print((n+(n*0.20))/n2)



