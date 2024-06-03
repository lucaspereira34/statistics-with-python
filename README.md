# Introduction

The goal of this project is to explore the use of statistical tools with Python providing a material for both Python and Statistics students. 

We'll study a research with data from brazilian families raised by IBGE (Brazilian Institute of Geography and Statistics).

Data source: https://www.ibge.gov.br/estatisticas/sociais/trabalho/9127-pesquisa-nacional-por-amostra-de-domicilios.html?=&t=downloads

Following the data source link above, you should go to "microdados" and download the files in "2015" folder. The dataset we want to study is "PES2015.txt" in "Dados_20170517.zip" file. The data dictionary is "Dicionário de variáveis de pessoas - PNAD 2015.xlsx" in "Dicionarios_e_input_20170517.zip".

# Managing the dataset

After downloading the files, we have all the data from the research in a raw format. In the next steps, we'll show how to handle this data. 

The code used in this section is in "readData.py" file.  After executing this python script, we expect to have created a file "data.csv" with the data we'll study.

## Selecting variables

The first step is to select what information we want. 

In this project, we'll focus on the income of people of reference in brazilian residences. It's recommended to select a group of categorical variables to enrich our analysis. 

After checking the data dictionary, we selected the following variables:

- Federal Unit (_Unidade da Federação_)
- Gender (_Sexo_)
- Age (_Idade_)
- Status in the residence (_Condição no domicílio_) - **_this variable is needed to filter only registers from the people of reference._**
- Color (_Cor ou raça_)
- Monthly income in cash (_Rendimento mensal em dinheiro_)
- Years of study (_Anos de estudo_)

## Storing the dataset

To store the dataset, we'll use _DataFrame_ structure from pandas library.

~~~python
# import pandas library
import pandas as pd

# read the file and store it in 'file' dataframe
file = pd.read_csv('PES2015.txt', header=None)
~~~

The dataset file "PES2015.txt" is too large for github, so you have to download it from the data source link and store it in your local repository.

## Creating column variables

This dataset stores information by position. According to the dictionary, the data we selected are in the following positions (starting in 1):

| Starting position | Length | Description |
| ----------------- | ------ | ----------- |
| 5 | 2 | Federal Unit |
| 18 | 1 | Gender |
| 27 | 3 | Age |
| 30 | 1 | Status in the residence |
| 33 | 1 | Color |
| 327 | 12 | Monthly income |
| 703 | 2 | Years of study |

Each index of the _file_ DataFrame is a string object with all the information in a single column. Therefore, we can access the desired variables using string manipulation and store them in an empty dataframe.

It's important to remember that positions in strings start in 0, so we have to use the starting position from the dictionary minus one.

~~~python
# create empty 'df' dataframe
df = pd.DataFrame()

# create 'df' columns based on position reference
df['Federal_unit'] = file[0].str[4:6]
df['Gender'] = file[0].str[17:18]
df['Age'] = file[0].str[26:29]
df['Status_in_residence'] = file[0].str[29:30]
df['Color'] = file[0].str[32:33]
df['Income'] = file[0].str[326:338]
df['Years_of_study'] = file[0].str[702:704]
~~~

## Applicating filters and transformations

Now that we have our variables separated by columns, the next step is to applicate the filters we want and handle the undesireble formats and values.

We'll store the manipulated data in a new dataset named _data_.

### Considering only registers from people of reference

According to the data dictionary, these are the possible values for the _Status_in_residence_ variable:

| Value | Description |
| ----- | ----------- |
| 1	| Person of reference (_Pessoa de referência_) |
| 2	| Spouse (_Cônjuge_) |
| 3	| Son (_Filho_) |
| 4	| Another relative (_Outro parente_) |
| 5	| Unreletad person (_Agregado_) |
| 6	| Guest (_Pensionista_) |
| 7	| Housekeeper (_Empregado doméstico_) |
| 8	| Housekeeper relative (_Parente do empregado doméstico_) |

Since we want only registers from the people of reference, we filter Status_in_residence==1 using _DataFrame.loc_. After this, the Status_in_residence column is no longer needed and we can drop it.

~~~python
# create 'data' dataframe only with registers from people of reference
data = df.loc[df['Status_in_residence']=='1']

# drop 'Status_in_residence' column
data = data.drop(columns='Status_in_residence')
~~~
