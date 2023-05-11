#Fazer um programa em python que pergunta um valor em metros e imprime o correspondente em decímetros, centímetros e milímetros.

def valores(metro):
    decimetro = metro * 10
    centimetro = metro * 100
    milimetro = metro * 1000
    return decimetro,centimetro,milimetro
def verValores(decimetro,centimetro,milimetro):
    print("O valor em decimetros é: ",decimetro)
    print("O valor em centimetros é: ",centimetro)
    print("O valor em milimetros é: ",milimetro)
def main():
    decimetro = 0
    centimetro = 0
    milimetro = 0
    metro = float(input("Digite um valor em metros: "))
    decimetro,centimetro,milimetro = valores(metro)
    verValores(decimetro,centimetro,milimetro)
main()

#Faça um programa que receba a idade e o peso de 7 pessoas, calcule e mostre:

