time=[]
jg={}
gol=[]
while True:
    jg.clear()
    jg['JOGADOR']=str(input('Nome do Jogador:'))
    jg['PARTIDAS']=int(input('Informe o número de patidas do jogador:'))
    gol.clear()
    cont=1
    for i in range(0,jg['PARTIDAS']):
        pg=int(input(f'Número de gol na {cont}ª partida:'))
        gol.append(pg)
    jg['GOL']=gol.copy()
    cont=cont+1
    s=sum(gol)
    jg['TOTAL']=s
    time.append(jg.copy())
    while True:
        resp=str(input('DESEJA CONTINUAR? (S/N)')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! UTILIZE S OU N')
    if resp == 'N':
         break
print('-'*60)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for c in v.values():
        print(f'{str(c):<20} ', end='')
    print()


print('-'*60)


