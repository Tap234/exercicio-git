nomes = []
nomes_exame = []
medias = []
notas_exame = []
with open ("exame.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        try:
            numeros = linha.strip()
            medias.append(float(numeros))
        except ValueError:
            pass
    for linha in linhas:
        nomes.append(linha.strip())
nomes_exame = nomes[::2]
for i in range(len(nomes_exame)):
    nome = nomes_exame[i]  
    while (True):
        a = float(input(f"Digite a nota do {nome}:"))
        notas_exame.append(a)
        break
for i in range(len(nomes_exame)):
    nome = nomes_exame[i]
    media = medias[i]
    nota_exame = notas_exame[i]
    sublista = [media , nota_exame]
    media_final = sum(sublista) / len(sublista)
    if media_final >= 5:
        with open("aprovados.txt", "r+") as arquivo_aprovados:
            arquivo.seek()
    print(f"{nome} {media_final}")
print(medias)
print(nomes_exame)
print(notas_exame)
print(media_final)