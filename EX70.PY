cont=0
s=0
total=0
mil=0
menor=0
maior=0
barato=''
while True:
    print("-"*30)
    print('LOJÃO DO FRAGOSO')
    print("-" * 30)
    p=str(input('NOME DO PRODUTO:')).strip().upper()
    preço=float(input('PREÇO DO PRODUTO:(R$)'))
    cont=cont=1
    total=total+preço
    if preço>1000:
        mil=mil+1
    elif cont==1 or preço < menor:
        menor=preço
        barato=p
    r=''
    while r not in 'SN':
        r=str(input('DESEJA REGISTRAR OUTRO PRODUTO?[S/N]')).strip().upper()[0]
    if r=="N":
        break
print(total)
print(mil)
print(menor)
print(barato)