def mostratNaTela():
    print("Olá mundo!")
    print("fim do programa")

# mostratNaTela()

def somaNumeros(n1, n2):
    print(f'a soma dos numeros é {n1 + n2}')

def retornaMaior(*list):
    # print(list)
    print(max(list))
    print(min(list))

# somaNumeros(10, 20)
# somaNumeros(n2 = 20, n1 = 10)

retornaMaior(1, 2, 3, 4, 50, 90, 30, 80)