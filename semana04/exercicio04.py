#Faça um algoritmo que leia dois valores e apresente:
#O maior deles
#O menor deles

#Obs. o algoritmo deve verificar se os valores digitados são iguais

n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))

if n1 > n2:
    print("O maior valor é:", n1)
    print("O menor valor é:", n2)
elif n2 > n1:
    print("O maior valor é:", n2)
    print("O menor valor é:", n1)
else:
    print("Os valores são iguais")
