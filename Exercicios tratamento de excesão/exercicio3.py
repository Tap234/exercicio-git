class ExcecaoZero(Exception):
    pass


try:
    a = int(input("Digite um número inteiro"))
    if a != 0:
        print("Seu resultado foi", a / 10)
    else:
        raise ExcecaoZero
except ExcecaoZero:
    print("O número digitado não pode ser 0")
