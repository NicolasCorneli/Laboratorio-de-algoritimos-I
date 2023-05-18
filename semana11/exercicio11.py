def y(valores):
    for x in range (1,11):
        valor = int(input("Digite um valor: "))
        valores.append(valor)
def z(valores):
    for x in valores:
        if x > 100:
            print(x)
def main():
    valores = []
    y(valores)
    z(valores)
    
main()
