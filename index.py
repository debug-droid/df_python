import pandas as pd

#lendo o arquivo notas_alunos
df = pd.read_csv(r"C:\Users\Diego\Desktop\python_\df_python\notas_alunos.csv")

#calculo da média
df["media"] = (df["nota_1"]+ df["nota_2"])/2

#condição para aprovado ou reprovado
df.loc[df["media"] >= 7, "situacao"] = "APROVADO"

df.loc[df["media"] < 7 , "situacao"] = "REPROVADO"

df.loc[df["faltas"] > 5, "situacao"] = "REPROVADO"

alunos_situacao=df

#imorimindo a tabela
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
df.to_csv(r"C:\Users\Diego\Desktop\python_\df_python\alunos_situacao.csv")