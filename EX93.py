jg={}
gol=[]
jg['JOGADOR']=str(input('Nome do Jogador:'))
jg['PARTIDAS']=int(input('Informe o número de patidas do jogador:'))
jg['GOLS']=gol
cont=1
for i in range(0,jg['PARTIDAS']):
    pg=int(input(f'Número de gol na {cont}ª partida:'))
    gol.append(pg)
    cont=cont+1
s=sum(gol)
jg['TOTAL']=s
print('=-'*50)
print(jg)
print('=-'*50)
print(f'O jogador {jg["JOGADOR"]} participou de {jg["PARTIDAS"]} partidas.')
for i in range(0,jg['PARTIDAS']):
    print(f'==>Na {i+1}ª partida, fez {gol[i]} gols.')
