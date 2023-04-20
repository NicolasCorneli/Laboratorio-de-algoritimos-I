#Faça um programa que exiba na tela os números de 1 a 10 utilizando o laço de repetição for.

for x in range(1,11):
    print(x)
    
#Crie um programa que calcule e exiba na tela a média aritmética de um conjunto de números lidos do usuário utilizando o laço de repetição for.

contador = 0
soma = 0
primeiro = int(input("Digite o primeiro número: "))
segundo = int(input("Digite o segundo número: "))
for x in range(primeiro+1,segundo):
    soma = soma + x
    contador = contador + 1
    media = soma / contador
print("A média dos valores entre os números digitados é: ",media)

#Escreva um programa que imprima na tela a sequência de Fibonacci até o décimo termo utilizando o laço de repetição for.

primeiro = 0
segundo = 1
for x in range(3,11):
    proximo = primeiro + segundo
    print(proximo)
    primeiro = segundo
    segundo = proximo
    
#Faça um algoritmo que leia 10 números inteiros e ao final apresente:
#Quantidade de números pares digitados
#Quantidade de números ímpares digitados
#Quantidade de zeros digitados

