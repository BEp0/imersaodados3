import pandas as pd

url_dados = 'https://github.com/BEp0/imersaodados3/blob/main/dados/dados_experimentos.zip?raw=true'

dados = pd.read_csv(url_dados, compression = 'zip')

#destino_drogas = open('/home/souza/Documents/Programas-GitHub/imersaodados3/dados/dismenbrando_dados/drogas.csv', 'w')
'''for i in dados:
    destino_drogas.write(dados['droga'].unique())

destino_drogas.close()'''
