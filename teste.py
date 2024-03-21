nomes = []
medias = []
with open("exame.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        try:
            media = float(linha.strip())
            medias.append(media)
        except ValueError:
            nomes.append(linha.strip())

dados_alunos = {}
for i in range(len(nomes)):
    nome = nomes[i]
    media = medias[i]
    if nome in dados_alunos:
        dados_alunos[nome].append(media)
    else:
        dados_alunos[nome] = [media]

for nome, medias in dados_alunos.items():
    while True:
        nota_exame = float(input(f"Digite a nota do {nome} no exame: "))
        if nota_exame >= 0 and nota_exame <= 10:
            medias.append(nota_exame)
            break
        else:
            print("Nota inválida. A nota do exame deve estar entre 0 e 10.")

    media_final = sum(medias) / len(medias)
    print(f"Média de {nome}: {media_final}")
