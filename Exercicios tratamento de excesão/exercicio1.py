class Excecaoimpar (Exception):
    pass


try:
    a = int(input("Digite um numero inteiro."))
    if a % 2 == 0:
        print("Seu número é par")
    else:
        raise Excecaoimpar("O numero não pode ser impar")
except Excecaoimpar as e:
    print(e)
except ValueError:
    print("O valor informado não é um número inteiro")
