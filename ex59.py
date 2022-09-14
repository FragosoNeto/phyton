import time

print('####CALCULADORA###')
op=0
valor1=int(input('INFORME O PRIMEIRO VALOR: '))
valor2=int(input('INFORME O SEGUNDO VALOR: '))
while op!=5:
    print('###OPERAÇÕES###')
    time.sleep(0.3)
    print('[1] SOMA')
    time.sleep(0.3)
    print('[2] MULTIPLICAÇÃO')
    time.sleep(0.3)
    print('[3] MAIOR VALOR')
    time.sleep(0.3)
    print('[4] NOVA ENTRADA')
    time.sleep(0.3)
    print('[5] SAIR')
    time.sleep(0.3)
    op=int(input('ESCOLHA UMA OPÇÃO: '))
    if op==1:
        soma=valor1+valor2
        print('-'*30)
        print(f'A SOMA ENTRE OS VALORES É: {soma}')
        print('-' * 30)
    elif op==2:
        mult=valor1*valor2
        print('-'*30)
        print(f'A SOMA ENTRE OS VALORES É: {mult}')
        print('-' * 30)
    elif op == 3:
        maior=0
        if valor1>valor2:
            maior=valor1
            print('-' * 30)
            print(f'O MAIOR NÚMERO É: {maior}')
            print('-' * 30)
        else:
            maior=valor2
            print('-' * 30)
            print(f'O MAIOR NÚMERO É: {maior}')
            print('-' * 30)
    elif op == 4:
        valor1 = int(input('INFORME O PRIMEIRO VALOR: '))
        valor2 = int(input('INFORME O SEGUNDO VALOR: '))
    elif op == 5:
        time.sleep(0.5)
        print('FINALIZANDO.....')
        time.sleep(0.5)
        print("FIM")
    else:
        print('-' * 30)
        print(f'OPÇÃO INVÁLIDA. TENTE NOVAMENTE')
        print('-' * 30)


