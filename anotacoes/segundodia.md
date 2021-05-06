# 2º dia:
### [Link para o notebook do 2º dia](https://github.com/BEp0/imersaodados3/blob/main/arquivos_calab/dia2.ipynb)

Neste dia, iniciamos o vídeo com a apresentação da lib Seaborn, que é uma biblioteca para criação de gráficos

> Não irei mensionar os comandos usados como fiz na primeira aula, mas deixei tudo documentado na pasta arquivos_colab.

---

## Desafios:
1. Ordenar o gráfico countplot.
2. Melhorar a visualização alterando tamanho da fonte etc.
3. Resumo do que você aprendeu com os dados

---

## Resumindo:
Foi nos apresentado como transformar o nome de uma coluna, através de um mapa,
 juntamente de alguns parâmetros como o `inplace=True`, 
 que atualiza o data frame com o rename que nos demos.
Também, nos foi apresentado o método `.query()` que foi dado como desafio do dia anterior. Segue abaixo outras coisas que foram apresentadas nesse dia:

- Como aumentar o tamanho do gráfico usando `plt.figure(figsize=(x, y))`
- Como adicionar um título usando `set_title()`
- Como aumentar esse título, passando como parâmetro `fontsize=X`, onde X é o tamanho da fonte
- Como tirar a parte da tabela "Text" e deixar ela mais bonitinha
- Como colocar nome nos eixos X e Y usando `set_xlabel()` e `set_ylabel()`
- Como fazer um historiograma com `.hist(bins=80)`
- Como descrever todos os elementos transformando as colunas em linhas com `.loc[0:, 'primeiro':'ultimo'].describe().T`

