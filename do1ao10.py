"""exo2 Curso em vídeo Python
nome = input("Digite seu nome:")
print("É um prazer te conhecer, %s" % nome)"""

"""exo 3
v1 = int(input("Digite um valor:"))
v2 = int(input("Digite outro valor:"))
soma = v1 + v2
print("A soma entre {} e {} é igual a {}".format(v1,v2,soma))"""

"""exo 4 DISSECANDO VARIAVEL
a = input("Digite algo:")
print("O tipo primitivo desse valor é", type(a))
print("Só tem espaço?", a.isspace())
print("É um número?", a.isnumeric())
print("É um alfabetico?", a.isalpha())
print("Está em maiúsculo?", a.isupper())
print("Está em minúsculo?", a.islower())"""

"""exo 5
n = int(input("Digite um número:"))
a = n-1
s = n+1
print("Analisando o valor {}, seu antecessor é {} e o sucessor é {}".format(n,a,s))"""

"""exo 6 POTENCIA E RAIZ
n = int(input("Digite um número:"))
print(" O dobro de {} vale {}\n O triplo vale {}\n A raiz quadrada é {}".format(n, (n*2),(n*3),pow(n,(1/2))))"""

"""exo 7 MÉDIA
n1 = float(input("Primeira nota do aluno: "))
n2 = float(input("Segunda nota do aluno: "))
m = (n1+n2)/2
print("A média entre {:.1f} e {:.1f} é igual a {:.1f}".format(n1,n2,m))"""

"""exo8 CONVERSÃO
d = float(input("Uma distância em metros:"))
cm = d * 100
km = d /1000
print("A medida {}m corresponde a {:.1f}cm ou {}km".format(d,cm,km))"""

"""exo9 TABUADA
t = int(input("Digite um número para ver sua tabuada: "))
print('-' * 12)
aux = 0
while aux<10:
    aux = aux + 1
    print("{} x {} = {}".format(t,aux,(t*aux)))
print('-' * 12)"""

"""exo10 CONVERSÃO
real = float(input("Quanto dinheiro voce tem na carteira? R$"))
dolar = real/(4.09)
print("Com R${:.2f} voce pode comprar U${:.2f}".format(real,dolar))"""
