notas = []
medias = []
nomes = []
nomes_alunos = []
with open ("notas.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        try:
            numeros = linha.strip()
            notas.extend(map(float, numeros))
        except ValueError:
            pass
    for linha in linhas:
        nomes.append(linha.strip())
for i in range(0, len(notas), 3):
    sublista = notas[i: i+3]
    media = sum(sublista) / len(sublista)
    medias.append(media)
nomes_alunos = nomes[::4]
for i in range(len(nomes_alunos)):
    nome = nomes_alunos[i]
    medias_alunos = medias[i]
    print(f"{nome}, {medias_alunos}")    
print(notas)
print(medias)
print(nomes_alunos)
