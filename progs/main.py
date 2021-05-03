import pandas as pd

url_dados = 'https://github.com/BEp0/imersaodados3/blob/main/dados/dados_experimentos.zip?raw=true'

dados = pd.read_csv(url_dados, compression = 'zip')

#print(dados['tratamento'].unique())
print(dados.head())
# dados['tratamento']
# dados['tratamento'].unique()
# dados['tempo'].unique()
