class ExcecaoMinuscula (Exception):
    pass


try:
    a = input(str("Digite letras"))
    if a.isupper():
        print("Todas as letras são maiúsculas")
    else:
        raise ExcecaoMinuscula
except ExcecaoMinuscula:
    print("Não pode haver letras minúsculas")
