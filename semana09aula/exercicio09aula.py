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

def media(mediaIdade,mediaPeso,idade,peso):
    for x in range (1,8):
        idade = int(input("Digite sua idade: "))
        peso = float(input("Digite seu peso: "))
        mediaIdade = mediaIdade + idade
        mediaPeso = mediaPeso + peso
    mediaIdade = mediaIdade / 7
    mediaPeso = mediaPeso / 7
    print("media idade:",mediaIdade)
    print("media peso: ",mediaPeso)
    return idade
def maiorIdade(idade,qntdMaior):
    if idade >= 18:
        qntdMaior = qntdMaior + 1
    print("quantidade de maiores de idade:",qntdMaior)
    
def porcentagem(idade,porcentagemIdades):
    if idade > 10 and idade < 30:
        porcentagemIdades = porcentagemIdades + 1
    porcentagemIdades = porcentagemIdades / 7
    porcentagemIdades = porcentagemIdades * 100
    print("porcentagem das idades entre 10 e 30:",porcentagemIdades)
    
def main():
    peso = 0
    idade = 0
    mediaPeso = 0
    mediaIdade = 0
    qntdMaior = 0
    porcentagemIdades = 0
    idade = media(mediaIdade,mediaPeso,idade,peso)
    maiorIdade(idade,qntdMaior)
    porcentagem(idade,porcentagemIdades)
main()
