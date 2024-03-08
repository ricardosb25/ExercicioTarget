def fibonacci(num):
    x = 0
    y = 1

    if num <= 2 & num >-1:
        return True
    
    while y < num:
        z = x + y
        x = y
        y = z
    return y == num

print("Programa que verifica se numero pertence a sequencia de Fibonacci")
try:
    numero = int(input("Digite um numero inteiro: "))

    if fibonacci(numero):
        print(f"{numero} pertence a sequencia de Fibonacci")
    else:
        print(f"{numero} não pertence a sequencia de Fibonacci")

except ValueError:
    print("Erro, insira um numero inteiro positivo")