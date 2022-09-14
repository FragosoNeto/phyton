import pandas as pd

trt13=pd.read_csv('servidores.csv')
trt13['Total']=trt13['Total'].astype(float)
dcc=0
soma_dcc=0
acc=0
soma_acc=0
dta=0
soma_dta=0
des=0
soma_des=0
dpm=0
soma_dpm=0
for i in range(0,len(trt13["Lotacao"])):
    xdcc = trt13['Lotacao'][i]
    if xdcc=="GABINETE DO DESEMBARGADOR CARLOS COELHO DE MIRANDA FREIRE":
        dcc = dcc + 1
        sl_dcc = trt13['Total'][i]
        soma_dcc = sl_dcc + soma_dcc

for i in range(0,len(trt13["Lotacao"])):
    xacc = trt13['Lotacao'][i]
    if xacc=="GABINETE DO DESEMBARGADOR FRANCISCO DE ASSIS CARVALHO E SILVA":
        acc=acc+1
        sl_acc=trt13['Total'][i]
        soma_acc=sl_acc+soma_acc

for i in range(0,len(trt13["Lotacao"])):
    xdta = trt13['Lotacao'][i]
    if xdta=="GABINETE DO DESEMBARGADOR THIAGO DE ANDRADE":
        dta=dta+1
        sl_dta=trt13['Total'][i]
        soma_dta=sl_dta+soma_dta

for i in range(0,len(trt13["Lotacao"])):
    xdes = trt13['Lotacao'][i]
    if xdes=="GABINETE DO DESEMBARGADOR EDUARDO SÉRGIO DE ALMEIDA":
        des=des+1
        sl_des=trt13['Total'][i]
        soma_des=sl_des+soma_des

for i in range(0,len(trt13["Lotacao"])):
    xdpm = trt13['Lotacao'][i]
    if xdpm=="GABINETE DO DESEMBARGADOR PAULO AMERICO MAIA DE VASCONCELOS FILHO":
        dpm=dpm+1
        sl_dpm=trt13['Total'][i]
        soma_dpm=sl_des+soma_dpm


print('\n-------ÁREA JUDICIÁRIA 2º GRAU----------')

print('\n\n---DADOS DO GABINETE DO DES. CARLOS COELHO ->')
print(f"Número de servidores do GDCC:{dcc}")
print("Custo do GDCC:{:.2f}\n".format(soma_dcc))

print('---DADOS DO GABINETE DO DES. ASSIS CARVALHO ->')
print(f"Número de servidores do GDACC:{acc}")
print("Custo do GDACC:{:.2f}\n".format(soma_acc))

print('---DADOS DO GABINETE DO DES. THIAGO DE ANDRADE ->')
print(f"Número de servidores do GDTA:{dta}")
print("Custo do GDTA:{:.2f}\n".format(soma_dta))

print('---DADOS DO GABINETE DO DES. EDUARDO SERGIO ->')
print(f"Número de servidores do GDES:{des}")
print("Custo do GDES:{:.2f}\n".format(soma_des))

print('---DADOS DO GABINETE DO DES. PAULO MAIA ->')
print(f"Número de servidores do GDPM:{dpm}")
print("Custo do GDPM:{:.2f}\n".format(soma_dpm))