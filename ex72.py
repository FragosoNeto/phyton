ex=('zero', 'um', 'dois', 'trê', 'quatro', 'cinco', 'seis', 'sete','oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatoze', 'quinze', 'desesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n=int(input("Digite um número de 0 a 20:"))
    if n>20 or n<0:
        print('Erro!Numeração fora do intervalo')
    else:
       print(f'O número por extenso é {ex[n]}')
       break


