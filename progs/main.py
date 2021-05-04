import pandas as pd
import matplotlib.pyplot as plt


def graficos(dose):

    # ---- gráfico das doses ----
    dose.plot.bar()
    plt.title('GRÁFICO DAS DOSES:')
    plt.ylabel('TIPOS DE DOSES')

    # ---- grádico do tratamento ----
    tratamento.plot.bar()
    plt.title('Tipos de Tratamento', fontsize=16)


def main():
    # receber os dados da imersão
    url_dados = 'https://github.com/BEp0/imersaodados3/blob/main/dados/dados_experimentos.zip?raw=true'

    # atribuir os dados a variável
    dados = pd.read_csv(url_dados, compression = 'zip')

    # tratando os dados
    tratados = dados[dados['g-0'] > 0]
    tratamento = dados['tratamento'].value_counts()
    valor_droga = dados['droga'].unique()
    id_dados = dados['id'].unique()
    dose = dados['dose'].unique()

    # gerar gráficos
    graficos(dose)

    # reatribuir os nomes de, por exemplo,  "g-0" para "g0"
    for i in range(0, 35):
        mapa = {f'g-{i}': f'g{i}'}
        dados.rename(columns=mapa, inplace=True)


if __name__ == "__main__":
    main()