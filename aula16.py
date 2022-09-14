t=('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    d = int(input('Digite um número de 0 a 20:'))
    if d<0 or d>20:
        print('Tente novamente')
    else:
        p = t[d]
        break

print(f'O extenso do número é {p}')


