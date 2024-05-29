# Solicita ao usuário o último número a ser impresso
fim = int(input("Digite o último número a imprimir:"))

# Inicializa a variável x como 1
x = 1

# Loop para imprimir os números ímpares até o número inserido pelo usuário
while x <= fim:
    print(x)
    x = x + 2
