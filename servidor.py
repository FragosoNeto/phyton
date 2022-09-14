import pandas as pd
soma=0
cont=0
cont1=0
while True:
    if pd.sevidores[grau][cont]==1:
        cont=cont+1
        if pd.sevidores[admjud][cont1]==1:
            soma=soma+1
            cont1=cont1+1
    else:
        break
print(soma)