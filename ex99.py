import time
def maior():
    list=[]
    cont=0
    while True:
        n=(int(input(f'Digite {cont}º valor: - para concluir digite 999:')))
        cont=cont+1
        list.append((n))
        if n==999:
            list.pop()
            break
    print("=-"*50)
    print("Analisando os valores!!!!!!")
    print(f"Foram informados {len(list)} valores, os quais são:{list}, tendo como maior {max(list)}!!!!!")
    print("=-" * 50)


maior()