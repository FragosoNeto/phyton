import datetime
a=datetime.datetime.today().year
a1=int(a)
print(a)
x=0
for i in range(1,7):
    n=int(input(f'Ano de nascimen da {i}ª pessoa:'))
    if (a1-n)>=18:
        x=x+1
print(f'{x} pessoa(s) são(é) maior(es) de idade')
print(f'{6-x} pessoa(s) são(é) menor(es) de idade')











