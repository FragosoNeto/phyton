import datetime
def eleitoral(a):
    hj=datetime.datetime.now().year
    idade=hj-a
    if idade>=18 and idade<70:
        print("Seu voto é obrigatório")
    elif idade<16:
        print("Você não pode votar")
    else:
        print("Seu voto é opcional.")

print("--"*30)
ano=int(input("Informe a data de nascimento:"))
eleitoral(ano)
print("--"*30)
