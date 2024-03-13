class ExcecaoString (Exception):
    pass


try:
    a = str(input("Digite uma string"))
    b = str(input("Digite outra string"))
    if len(a) == len(b):
        print("As suas strings possuem o mesmo comprimento")
    else:
        raise ExcecaoString
except ExcecaoString:
    print("Não pode haver duas strings de diferentes comprimento")
    
