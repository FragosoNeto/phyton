p=float(input('Digite o seu peso:'))
h=float(input('Digite sua altura:'))
imc=float(p/h**2)
print('{:.2f}'.format(imc))
if 18.5>imc:
    print('Abaixo do Peso')
elif 18.5 <= imc< 25:
    print('Peso ideal')
elif 25<=imc<30:
    print('Sobrepeso')
elif 30<=imc<40:
    print('Obesidade')
else:
    print('Obesidade mórbida')


