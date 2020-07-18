def exercicio_1():
    print("""1) Faça um algoritmo que leia um número e  mostre se o mesmo é positivo, negativo ou zero.""")
    num1 = int(input("Digite aí o número: "))

    if(num1 > 0):
        print("É positivo!")
    elif(num1 < 0):
        print("É negativo!")
    else:
        print("É zero!")

def exercicio_2():
    print("2) Faça um algoritmo que leia um número e mostre se o mesmo é par ou ímpar.")
    num2 = int(input("Digite aí o outro número: "))

    if(num2 % 2 == 0):
        print("É par!")
    else:
        print("É ímpar!")

def exercicio_3():
    print("3) Faça um algoritmo que leia dois números e imprima o maior.")
    n1 = int(input("Digite aí o primeirão: "))
    n2 = int(input("Digite aí o segundão: "))

    if(n1 > n2):
        print(str(n1), "é maior que",str(n2))
    elif(n2 > n1):
        print(str(n2), "é maior que",str(n1))
    else:
        print(str(n1), "é igual a",str(n2))

def exercicio_4():
    print("4) Faça um algoritmo que peça a idade de uma pessoa e imprima na tela se a mesma já é maior de idade ou então, se a mesma é de menor.")
    idade = int(input("Digite sua idade: "))
    if(idade >= 18):
        print("É maior, pode entrar no show!")
    else:
        print("É menor. Tente outa vez quando você fizer 18 anos.")

def exercicio_5():
    print("5) Faça um algoritmo que peça a idade do usuário e a idade da sua mãe. Em seguida, imprima na tela com quantos anos sua mãe o teve.")
    idadeUsuario = int(input("Digite sua idade: "))
    idadeMae = int(input("Quantos anos sua mãe tem hoje? "))
    print("Sua mãe tinha",str(idadeMae-idadeUsuario),"quando você nasceu.")

    print("6) Faça um algoritmo que imprima 50 vezes o caractere - na tela (sem a utilização de laços de repetição).")
    a = 50 * "-"
    print(a)

def exercicio_9():
    print("9) Faça um algoritmo que verifica se um determinado valor é um número inteiro.")
    confereInt = input("Digite um valor qualquer: ")
    try:
        converteValor = int(confereInt)
        print(str(converteValor), "é um número inteiro.")
    except ValueError:
        try:
            converteValor = float(confereInt)
            print(str(converteValor), "é um número float.")
        except ValueError:
            print(str(confereInt), "é uma string.")

def exercicio_13():
    print("13) Faça um algoritmo que leia três números e imprima na tela o maior deles.")
    ar = list(map(int, input("Digite 3 números, separados por espaço e pressione enter: ").rstrip().split()))
    ar.sort(reverse=True)
    print(ar[0])

def exercicio_14():
    print("14) Faça um algoritmo que leia três números e imprima-os em ordem crescente.")
    ar = list(map(int, input("Digite 3 números, separados por espaço e pressione enter: ").rstrip().split()))
    ar.sort()
    print("Aqui estão os números: ",str(ar))

def exercicio_15():
    print("15) Faça um algoritmo que leia um caractere e informe se o mesmo é uma vogal ou não.")
    confereVogal = input("Digite uma letra: ")
    if('a' == confereVogal or 'A' == confereVogal or 'e' == confereVogal or 'E' == confereVogal or 'i' == confereVogal
     or 'I' == confereVogal or 'o' == confereVogal or 'O' == confereVogal or 'u' == confereVogal or 'U' == confereVogal):
        print("É uma vogal!")
    else:
        print("Não é uma vogal.")

def exercicio_16():
    print("16) Os endereços IP versão 4 são divididos em cinco classes: A, B, C, D e E."
    +"Os endereços no intervalo de 0 à 127 são classe A, de 128 a 191 são classe B, de 192 a 223 são classe C"
    +", de 224 à 239 são classe D e a partir de 240 são classe E. Faça um algoritmo que leia o primeiro octeto"
    +", no formato decimal de um endereço IP, e informe a sua classe.")
    print()
    primeiroOcteto = int(input("Digite os primeiros 3 dígitos do IP. (Ex.: 192): "))
    if(0 <= primeiroOcteto <= 127):
        print(str(primeiroOcteto),"é de classe A.")
    elif(128 <= primeiroOcteto <= 191):
        print(str(primeiroOcteto),"é de classe B.")
    elif(192 <= primeiroOcteto <= 223):
        print(str(primeiroOcteto),"é de classe C.")
    elif(224 <= primeiroOcteto <= 239):
        print(str(primeiroOcteto),"é de classe D.")
    elif(primeiroOcteto >= 240):
        print(str(primeiroOcteto),"é de classe E.")

def exercicio_17():
    print("17) Faça um algoritmo que receba um número inteiro, que represente um determinado mês do ano"
    +", e mostre o nome do mês correspondente. Por exemplo, se for informado o número 2, o algoritmo deverá exibir"
    +": fevereiro. O algoritmo também deve validar se a entrada está correta.")
    try:
        mes = int(input("Digite o número do mês: "))
        if(mes == 1):
            print("Janeiro")
        elif(mes == 2):
            print("Fevereiro")
        elif(mes == 3):
            print("Março")
        elif(mes == 4):
            print("Abril")
        elif(mes == 5):
            print("Maio")
        elif(mes == 6):
            print("Junho")
        elif(mes == 7):
            print("Julho")
        elif(mes == 8):
            print("Agosto")
        elif(mes == 9):
            print("Setembro")
        elif(mes == 10):
            print("Outubro")
        elif(mes == 11):
            print("Novembro")
        elif(mes == 12):
            print("Dezembro")
        else:
            print("Nenhum mês corresponde a esse valor.")
    except ValueError:
        print("O formato digitado está incorreto.")

def exercicio_18():
    print("18) Faça um algoritmo que valide uma data. A mesma deve ser formada por dia, mês e ano"
    +". Por exemplo, se o usuário digitar a data 10/8 a mesma será inválida"
    +". Porém, caso a data seja 01/10/2018, a mesma deve ser considerada válida.")
    data = input("Digite a data: ")
    import datetime
    formato = "%d/%m/%Y"
    try:
        datetime.datetime.strptime(data, formato)
        print(str(data),"é considerado um fomarto válido.")
    except ValueError:
        print(str(data),"não é considerado um fomarto válido.")




