notas = []
medias = []
with open("notas.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        try:
            numeros = linha.strip()
            notas.extend(map(float, numeros))
        except ValueError:
            pass

# Calcula as médias
for i in range(0, len(notas), 3):
    sublista = notas[i:i+3]
    media = sum(sublista) / len(sublista)
    medias.append(media)

print("Notas:", notas)
print("Médias:", medias)

# Extrai os nomes
nomes = notas[::4]
print("Nomes:", nomes)


