while(True):
    nome = str(input("Digite seu nome"))
    a = int(input("Digite sua primeira nota"))
    b = int(input("Digite sua segunda nota"))
    c = int(input("Digite sua segunda nota"))

    with open("notas.txt", "a") as arquivo:
        arquivo.write(f"{nome}\n")
        arquivo.write(f"{a}\n")
        arquivo.write(f"{b}\n")
        arquivo.write(f"{c}\n")
    if input("Deseja continuar?Sim = 1, Não = 2")!="1":
        break
