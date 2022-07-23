import pandas as pd

df = pd.read_csv(r"C:\Users\Diego\Desktop\python\notas_alunos.csv")

df.insert(4, 'media', [7.0,6.5,6.5,8.0])

df.insert(5, 'situacao', ["APROVADO","REPROVADO","REPROVADO","APROVADO"])
print(df)

maior_falta = df["faltas"].max()
print("O maior número de faltas foi: " + str(maior_falta))

media_alunos = df["media"].median()
print("Média geral das notas foi: " + str(media_alunos))

maior_media = df["media"].max()
print("A maior média é: " + str(maior_media))

df.to_csv(r"C:\Users\Diego\Desktop\python\alunos_situacao.csv")