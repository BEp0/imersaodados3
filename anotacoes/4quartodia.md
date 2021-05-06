# 4º dia:

### [Link para o notebook do 4º dia](https://github.com/BEp0/imersaodados3/blob/main/arquivos_calab/dia4.ipynb)
> Neste dia começamos a analisar a tabela de resultados


## O que foi feito:
Inicialmente, verificamos o que significava a grande quantidade de zeros que tinhamos na tabela resultados, logo, usando o unique(), identificamos que não havia somente o zero, mas também o valor 1, onde o 0 significa que o mecanismo da ação não foi ativado e o 1 significa que ele foi ativado.

Após isso, queriamos saber qual mecanismo de ação foi mais ativado, fizemos isso somando as colunas de acordo com cada linha, usando a forma abaixo:

    contagem_moa = dados_resultados.select_dtypes('int64').sum().sort_values(ascending=False)

Ao saber as repetições por linhas usando o comando `dados_resultados.drop('id', axis=1).sum(axis=1)`, queriamos saber quais dos resultados foram com controle e com droga.
Para isso, precisamos juntar as bases de dados, fazendo isso com uma função chamada merge, com isso criamos duas funções, a primeira que conta quantos ativos foram encontrado, e outra que mostra se foi encontrado ativo ou não, e atribuimos isso a duas novas colunas, nessa respectiva ordem.

Ao ter em mão essas novas colunas, realizei um for dentro da coluna nomeada "ativos_moa" para contas quantos False existiam, obtendo como respota o valor 9367, ou seja, sabemos agora que há 9367 zeros nessa coluna.

Apos o merge, usamos o `boxplot` para mostrar em um grafico os 5 componentes que mais aparecem, e com isso finalizamos o dia.

## Resumindo:

- Investigamos a base de dados de resultados.
- Entendemos os mecanismos mais ativados.
- Constatamos que um composto pode ativar mais de um mecanismo de ação.
- Vimos como juntar as bases usando merge.
- Criamos um boxplot