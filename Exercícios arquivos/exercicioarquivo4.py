notas_aprovados = []
notas_reprovados = []
nomes_aprovados = []
nomes_reprovados = []
with open ("aprovados.txt","r") as arquivo_aprovados:
    linhas = arquivo_aprovados.readlines()
    for linha in linhas:
        nomes_aprovados.append(linha.strip())
nomes_alunos_aprovados = nomes_aprovados[::2]
with open ("reprovados.txt","r") as arquivo_reprovados:
    linhas = arquivo_reprovados.readlines()
    for linha in linhas:
        nomes_reprovados.append(linha.strip())
nomes_alunos_reprovados = nomes_reprovados[::2]
print(nomes_alunos_reprovados)
print(nomes_alunos_aprovados)