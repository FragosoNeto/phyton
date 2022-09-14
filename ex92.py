import datetime
d={}
t=datetime.date.today().year
print(t)
nome=str(input('Nome:'))
d['nome']=nome
ano=int(input('Ano de Nascimento:'))
d['ano']=t-ano
carteira=int(input('Número da carteira de trabalho(0 não tem):'))
d['carteira']=carteira
if carteira > 0:
    contr=int(input('Ano da contratação:'))
    d['contr']=contr
    sal=float(input('Salário:(R$)'))
    d['sal']=sal
    ap=(35-(t-contr))+(t-ano)
    d['ap']=ap
else:
    print('CADASTRO REALIZADO COM SUCESSO')
for k,v in d.items():
    print(f'{k} tem o valor {v}')