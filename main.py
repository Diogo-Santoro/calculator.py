print(" Welcome to My Calculator / Bem vindo a Minha Calculadora! \n")
while 1:
    print("What would you like to do? / O que você quer fazer?")
    print("1. Addition / Adição")
    print("2. Subtraction / Subtração")
    print("3  Multiplication / Multiplicação")
    print("4. Division / Divisão")
    print("5. Exit / Sair")

    opcao = int(input("Enter your choice / Selecione sua opção: "))
    if opcao == 1:
        num1 = int(input("Enter first number / Digite seu primeiro número: "))
        num2 = int(input("Enter second number / Digite seu segundo número: "))
        print("Result / Resultado: ", num1+num2)
    elif opcao == 2:
        num1 = int(input("Enter first number / Digite seu primeiro número: "))
        num2 = int(input("Enter second number / Digite seu segundo número: "))
        print("Result / Resultado: ", num1-num2)
    elif opcao == 3:
        num1 = int(input("Enter first number / Digite seu primeiro número: "))
        num2 = int(input("Enter second number / Digite seu segundo número: "))
        print("Result / Resultado: ", num1*num2)
    elif opcao == 4:
        num1 = int(input("Enter first number / Digite seu primeiro número: "))
        num2 = int(input("Enter second number / Digite seu segundo número: "))
        print("Result / Resultado: ", num1/num2)
    elif opcao == 5:
        print("Exiting... / Saindo...")
        break
    print()