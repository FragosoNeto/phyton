pessoa={}
cadastro=[]
soma=0
media=0
while True:
    pessoa.clear()
    pessoa['nome']=str(input('Informe o nome do funcionário:')).upper()
    while True:
        pessoa['sexo']=str(input('Sexo:[M/F]')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! UTILIZE M OU F')
    pessoa['idade']=int(input('Idade:'))
    while True :
        c=str(input('DESEJA CONTINUAR?[S/N]')).upper()[0]
        if c in 'SN':
            break
        print('ERRO! UTILIZE S OU N')
    cadastro.append(pessoa.copy())
    if c == 'N':
        break
    print(cadastro)



















