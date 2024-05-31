def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Selecione a operação: ")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

choice = input("Escolha (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if choice == '1':
    result = add(num1, num2)
    print("O resultado da soma é:", result)
elif choice == '2':
    result = subtract(num1, num2)
    print("O resultado da subtração é:", result)
elif choice == '3':
    result = multiply(num1, num2)
    print("O resultado da multiplicação é:", result)
elif choice == '4':
    if num2 == 0:
        print("VOCÊ NÃO PODE DIVIDIR POR ZERO!")
    else:
        result = divide(num1, num2)
        print("O resultado da divisão é:", result)
else:
    print("Escolha inválida!")
