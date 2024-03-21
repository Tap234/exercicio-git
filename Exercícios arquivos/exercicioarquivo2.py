notas = []
medias = []
nomes = []
nomes_alunos = []
with open ("notas.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        try:
            numeros = linha.strip()
            notas.append(float(numeros))
        except ValueError:
            pass
    for linha in linhas:
        nomes.append(linha.strip())
for i in range(0, len(notas), 3):
    sublista = notas[i: i+3]
    media = sum(sublista) / len(sublista)
    medias.append(media)
nomes_alunos = nomes[::4]
with open("aprovados.txt", "w") as arquivo_aprovados, \
     open("exame.txt", "w") as arquivo_exame, \
     open("reprovados.txt", "w") as arquivo_reprovados:
    for i in range(len(nomes_alunos)):
        nome = nomes_alunos[i]
        medias_alunos = medias[i]
        if medias_alunos >= 7:
            arquivo_aprovados.write(f"{nome} \n{medias_alunos}\n")
        elif 7 > medias_alunos >= 5:
            arquivo_exame.write(f"{nome} \n{medias_alunos}\n")
        else:
            arquivo_reprovados.write(f"{nome} \n{medias_alunos}\n")
        print(f"{nome}, {medias_alunos}")

print(notas)
print(medias)
print(nomes_alunos)