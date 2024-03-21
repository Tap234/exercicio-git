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
nota_final = (sum(notas_exame[0] + medias[0])) / (len(notas_exame[0] + medias[0]))
print(medias)
print(nomes_exame)
print(notas_exame)
print(nota_final)