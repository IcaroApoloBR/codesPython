'''exo11 PAREDE DE TINTA
l = float(input("Largura da parede: "))
h = float(input("Altura da parede: "))
a = l*h
t = a/2
print("Sua parede tem a dimensão de {:.1f}x{:.2f} e sua área é de {:.3f}m²".format(l,h,a))
print("Para pintar essa parede, voce precisará de {:.5}l de tinta".format(t))'''

'''exo12 DESCONTO
p = float(input("Qual é o preço do produto? R$"))
d = p - (p*0.05)
print("O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}".format(p,d))'''

'''exo13 SALARIO
s = float(input("Qual é o salário do funcionário? R$"))
aum = s + s*0.15
print("Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}".format(s,aum))'''

'''exo14 TEMPERATURA
c = float(input("Informe a temperatura em ºC: "))
f = 1.8*c + 32
print("A temperatura de {:.1f}º corresponde a {:.1f}ºF".format(c,f))'''

'''exo15 ALUGAR CARROS
d = float(input("Quantos dias alugados? "))
km = float(input("Quantos km rodados? "))
total = d*60 + km*0.15
print("O total a pagar é de R${:.2f}".format(total))'''

'''exo16 NUMERO INTEIRO
num = float(input("Digite um valor: "))
print("O valor digitado foi {} e a sua porção inteira é {}".format(num, int(num)))'''

'''exo17 HIPOTENUSA
cop = float(input("Comprimento do cateto oposto: "))
cadj = float(input("Comprimento do cateto adjacente: "))
h = (cop ** 2 + cadj **2) ** (1/2)
print("A hipotenusa vai medir {:.2f}".format(h))'''

'''exo18ANGULOS
from math import radians, sin, cos, tan
ang = float(input("Digite o ângulo que voce deseja: "))
seno = sin(radians(ang))
print("O seno é {:.2f}".format(seno))
cosseno = cos(radians(ang))
print("O cosseno é {:.2f}".format(cosseno))
tangente = tan(radians(ang))
print("A tangente é {:.2f}".format(tangente))'''

'''exo19 SORTEIO
from random import choice
a1 = str(input("Primeiro aluno: "))
a2 = str(input("Segundo aluno: "))
a3 = str(input("Terceiro aluno: "))
a4 = str(input("Quarto aluno: "))
lista = [a1,a2,a3,a4]
escolhido = choice(lista)
print("O aluno escolhido foi {}".format(escolhido))'''

'''exo20 SORTEIO ORDEM
from random import shuffle
a1 = str(input("Primeiro aluno: "))
a2 = str(input("Segundo aluno: "))
a3 = str(input("Terceiro aluno: "))
a4 = str(input("Quarto aluno: "))
lista = [a1,a2,a3,a4]
shuffle(lista)
print("A ordem de apresentação será")
print(lista)'''




