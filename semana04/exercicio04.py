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
    
    #Um sistema de uma loja de roupas permite que as peças de roupas sejam vendidas de três formas diferentes: 
#À vista.
#2 vezes.
#3 vezes.
#Para isso, o sistema deve ler o valor da peça, a opção de pagamento e apresentar o valor das parcelas.

precoRoupa = float(input("Digite o valor do produto: "))

print("1 - À vista")
print("2 - Parcelar em 2 vezes")
print("3 - Parcelar em 3 vezes")
opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    print("O valor da roupa à vista é: ", precoRoupa)
elif opcao == 2:
    valorParcela = precoRoupa / 2
    print("O valor da roupa é: ", precoRoupa)
    print("O valor parcelado em 2 vezes é: ", valorParcela)
elif opcao == 3:
    valorParcela = precoRoupa / 3
    print("O valor da roupa é: ", precoRoupa)
    print("O valor parcelado em 3 vezes é: ", valorParcela)
else:
    print("Digite uma opção válida")
    
    
