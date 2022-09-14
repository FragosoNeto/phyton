dc={}
dc['Nome']=str(input('Digite o nome do aluno:'))
dc['Média']=float(input('Digite a média do aluno:'))
if dc['Média']>=7.0:
    dc['Situação'] = 'aprovado'
else:
    dc['Situação'] = 'recuperação'

print(dc)
