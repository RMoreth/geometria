import os


def circulo(raio):
    area = (3.14 * (raio ** 2))
    return area


def triangulo(base, altura):
    area = (base * altura) / 2
    return area


def trapezio(basinha, basao, altura):
    area = ((basinha + basao) * altura) / 2
    return area


while True:
    print("CALCULADOR DE ÁREA")
    print("Escolha o tipo: ")
    print("1 - circulo")
    print("2 - triangulo")
    print("3 - trapezio")
    tipo = int(input("digite o valor correspondente"))

    match tipo:
        case 1:
            os.system("cls")
            print("Calculando área do circulo")
            raio = float(input("Informe a medida do raio do circulo"))
            print(f"um circulo de raio={raio} tem área={circulo(raio)}")
        case 2:
            os.system("cls")
            print("Calculando área do triângulo")
            base = float(input("Informe a medida da base do triangulo"))
            altura = float(input("Informe a medida da altura do triangulo"))
            print(f"um triangulo de base={base} e altura={
                altura} tem área={triangulo(base, altura)}")
        case 3:
            os.system("cls")
            print("calculando área do trapezinho")
            basinha = float(
                input("Informe a medida da base menor do trapézio"))
            basao = float(input("Informe a medida da base maior do trapézio"))
            altura = float(input("Informe a medida da altura do trapézio"))
            print(f"um trapézio de base menor={basinha}, base maior={basao} e altura={altura} tem área={trapezio(basinha, basao, altura)}")
        case _:
            os.system("cls")
            print("valor digitado inválido")
    r = str(input("Deseja calcular outra área?[s/n]")).strip().lower()[0]

    if r == 'n':
        break
