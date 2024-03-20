# Lista de exemplo
lista = [10, 20, 30, 40, 50, 60, 70, 70, 70, 70, 70, 70, "c", 70, 70, 70]

# Lista para armazenar as médias
medias = []

# Loop para iterar pelos índices, pulando o primeiro e pegando os três seguintes
for i in range(1, len(lista), 4):
    # Verifica se há pelo menos três elementos restantes na lista
    
    indices = lista[i:i+3]
    media = sum(indices) / len(indices)
    medias.append(media)

print("Médias:", medias)
