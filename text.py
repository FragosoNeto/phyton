def cpf():
    cpfl=[]
    som=0
    som2=0
    while True:
        cpf = str(input('Digite o CPF(apenas número):')).strip().replace('.', '').replace('-', '')
        if len(cpf)==11 and cpf.isnumeric():
            for c in range(0,11):
                num=int(cpf[c])
                cpfl.append(num)
            for i in range(0,9):
                tot1=((cpfl[i]*(10-i)))
                som=som+tot1
            for i in range(0, 10):
                tot2 = ((cpfl[i] * (11 - i)))
                som2 = som2 + tot2
            tot_1 = som * 10 % 11
            tot_2 = som2 * 10 % 11
            if tot_1 == 10 :
                tot_1 = 0
            if tot_2 == 10 :
                tot_2 = 0
            while True :
                if tot_1 == cpfl[9] and tot_2 == cpfl[10] :
                    print(cpfl)
                    print(tot_1)
                    print(tot_2)
                    print('CPF VÁLIDO!')
                    break
                else:
                    raise ValueError("CPF inválido!")
                break
        else:
            raise ValueError("CPF inválido!")
        break


cpf()