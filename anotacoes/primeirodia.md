# 1º dia:

Neste dia o meu 1º desafio foi rodar o pandas no VSCode, que é o editor que eu uso, após algum tempo consequi sem muito trabalho.
Logo depois, acompanhei o vídeo disponibilizado pela alura e fui seguindo os passos, afim de exploração mesmo.

---

## Lista de alguns comandos usados no vídeo:

1. `pd.read_csv`
    
    - Lê ("read") um arquivo csv ("_csv")

2. `unique()`
    - Organiza por ordem e desnconsidera as repetições
    
    ex.: 

    ```
    lista = [ 1, 1, 0, 2, 5, , 6, 0, 4, 3 ]
    
    lista.inuque()

    #resultado:

        0, 1, 2, 3, 4, 5, 6

3. `compression = 'zip'`
    - É um parametro para indicar que o arquivo está em formato zip

4. `variável.head()`
    - Mostra somente os primeiros tópicos

5. `variável['nome da coluna']`
    - Podemos acessar os valores dentro de uma coluna usando esse método

6. `variável['nome da coluna'].value_count()`
    - Mostra a quantidade de repetições, conta as repetições

---

## Desafios dados no dia:

> Resolver os desafios com base na documentação do PANDAS

1. Porque há tanto com droga e pouco com controle? [ X ]
    - Ao meu ver, as chamadas "com_droga" são usadas para verificar a reação sem influência externas, logo as "com controle" são para verificar a reação em um cenário expecífico.

2. Plotar as 5 ultimas linhas da tabela [  ]

3. Proporção das classes tratamento [ X ]
    - Para identificar quanto tinhamos de "com_controle" e "com_dorga", fiz o seguite código:
    
    ```
    cd = dados['tratamento'].value_counts()[0]
    cc = dados['tratamento'].value_counts()[1]

    total = cd + cc

    porcentagem_cd = (cd * 100) / total
    porcentagem_cc = (cc * 100) / total

    porcentagem_cc, porcentagem_cd    # nos mostra a porcentagem
    ```
    - Desta forma, encontramos que os "com_droga" representam 92,16% do total. Já os "com_controle" representam 7,84%.

4. Quantas tipos de drogas foram investigados [ X ]
    - Na verdade não são drogas, mas sim vários compostos. Sabemos isso por conta do número de "drogas" que é muito alto.

5. Método query do pandas [  ]

6. Renomear as colunas [ X ]
    - Para renomear as colunas utilizei o seguinte método:
    
    ```for i in range(0, 35):
        mapa = {f'g-{i}': f'g{i}'}
        dados.rename(columns=mapa, inplace=True)
    ```
7. Deixar os gráficos com títulos [ X ]
    - Para adicionar título ao gráfico, usei o seguinte método:

    ```
    tratamento.plot.bar()
    plt.title('Tipos de Tratamento', fontsize=16)
    ```
8. Resumo do que aprendeu com os dados [  ]
