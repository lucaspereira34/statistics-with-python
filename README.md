## Introduction

The goal of this project is to explore the use of statistical tools with Python, providing a material for both Python and Statistics students. 

We'll study data from the heads of brazilian families. This dataset was raised by IBGE (Brazilian Institute of Geography and Statistics).

Data source: https://www.ibge.gov.br/estatisticas/sociais/trabalho/9127-pesquisa-nacional-por-amostra-de-domicilios.html?=&t=downloads

## Selecting data

Since our dataset is very large, the first step is to select what information we want to study. After checking the Dictionary, we can start with these variables:

- Federal Unit (_Unidade da Federação_)
- Gender (_Sexo_)
- Age (_Idade_)
- Status in the residence (_Condição no domicílio_)
- Color (_Cor ou raça_)
- Monthly income in cash (_Rendimento mensal em dinheiro_)
- Years of study (_Anos de estudo_)

## Creating our dataframe

This dataset stores information by position. According to the dictionary, the data we selected before are in the following positions:

| Starting position | Length | Description |
| ----------------- | ------ | ----------- |
| 5 | 2 | Federal Unit |
| 18 | 1 | Gender |
| 27 | 3 | Age |
| 30 | 1 | Status in the residence |
| 33 | 1 | Color |
| 119 | 12 | Monthly income |
| 703 | 2 | Years of study |
