import random
dc={}
l=[]

dc["jogador_1"]=random.randint(1,6)
dc["jogador_2"]=random.randint(1,6)
dc["jogador_3"]=random.randint(1,6)
dc["jogador_4"]=random.randint(1,6)
l.append(dc)
for k,v in dc.items():
    print(f'{k} - {v}')