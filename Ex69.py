op='S'
cont=0
dz=0
m=0
mv=0
while True:
    if op == 'S':
        print('-'*30)
        print('CADASTRE UMA PESSOA')
        print('-' * 30)
        sex=str(input('Sexo:[M/F]')).strip().upper()[0]
        idade=int(input('INFORME A IDADE:'))
        print('-' * 30)
        if idade>18:
            dz=dz+1
        elif sex=='F' and idade<20:
            mv=mv+1
        elif sex=='M':
            m=m+1
        op=str(input('CONTINUAR O CADASTRO[S/N]?')).strip().upper()[0]
    else:
        break
print(dz)
print(m)
print(mv)




