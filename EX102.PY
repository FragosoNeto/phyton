import math
def fatorial(a,b=False):
    n=a
    l=[]
    for i in range(n+1):
       l.append(i)
    l.pop(0)
    l.reverse()
    if b==True:
        for k,i in enumerate(l):
            print(f" {i} x", end="")
    print("=")
    f=math.factorial(n)
    print(f)


a=int(input("Digite um número:"))
fatorial(a, True)


