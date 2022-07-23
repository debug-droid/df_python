import pandas as pd

#lendo o arquivo notas_alunos
df = pd.read_csv(r"C:\Users\Diego\Desktop\python\notas_alunos.csv")

#inserindo a coluna media
df.insert(4, 'media', [7.0,6.5,6.5,8.0])

#inserindo a coluna situacao
df.insert(5, 'situacao', ["APROVADO","REPROVADO","REPROVADO","APROVADO"])
print(df)

#imprimindo o maior número de faltas
maior_falta = df["faltas"].max()
print("O maior número de faltas foi: " + str(maior_falta))

#imprimindo a média geral das notas
media_alunos = df["media"].median()
print("Média geral das notas foi: " + str(media_alunos))

#imprimindo a maior média
maior_media = df["media"].max()
print("A maior média é: " + str(maior_media))

#gerando arquivo alunos_situacao.csv
df.to_csv(r"C:\Users\Diego\Desktop\python\alunos_situacao.csv")