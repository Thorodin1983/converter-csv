import pandas as pd

##determinar caminho do arquivo##
df = pd.read_csv("C:\\Users\\lvasconcelos\\Desktop\\planilha que extraimos.csv")

##transformando arquivo csv para xlsx(formato tabela)
df.to_excel("ARQUIVOS\\dados.xlsx")
print("Material atualizado!")