import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# read data to dataframe
df = pd.read_csv('data.csv')

# dataframe overview
print('\n-------------------- Dataframe Overview --------------------\n\n', df.head(), '\n')

# qualitative nominal variables
gender = {0: 'Male', 1: 'Female'}
color = {0: 'Indigenous', 2: 'White', 4: 'Black', 6: 'Asian', 8: 'Brown', 9: 'Not declared'}
fu = {11: 'Rondônia', 12: 'Acre', 13: 'Amazonas', 14: 'Roraima', 15: 'Pará', 16: 'Amapá', 17: 'Tocatins',
      21: 'Maranhão', 22: 'Piauí', 23: 'Ceará', 24: 'Rio Grande do Norte', 25: 'Paraíba', 26: 'Pernambuco',
      27: 'Alagoas', 28: 'Sergipe', 29: 'Bahia', 31: 'Minas Gerais', 32: 'Espírito Santo', 33: 'Rio de Janeiro',
      35: 'São Paulo', 41: 'Paraná', 42: 'Santa Catarina', 43: 'Rio Grande do Sul', 50: 'Mato Grosso do Sul',
      51: 'Mato Grosso', 52: 'Goiás', 53: 'Distrito Federal'}

print('\n---------- Checking qualitative nominal variables ----------\n')
print('Gender: ', sorted(df.Gender.unique()), '\n\n', gender, '\n\n')
print('Color: ', sorted(df.Color.unique()), '\n\n', color, '\n\n')
print('Federal Unit (FU): ', sorted(df.Federal_unit.unique()), '\n\n', fu, '\n')

# qualitative ordinal variables
years_of_study = {1: 'No study or less than 1 year', 2: '1 year', 3: '2 years', 4: '3 years', 5: '4 years',
                  6: '5 years', 7: '6 years', 8: '7 years', 9: '10 years', 10: '9 years', 11: '10 years',
                  12: '11 years', 13: '12 years', 14: '13 years', 15: '14 years', 16: '15 or more years',
                  17: 'Not specified'}

print('\n---------- Checking qualitative ordinal variables ----------\n')
print('Years of study: ', sorted(df.Years_of_study.unique()), '\n\n', years_of_study, '\n')

# discrete quantitative variables
print('\n---------- Checking discrete quantitative variables ----------\n')
print('Age: %s to %s years' % (df.Age.min(), df.Age.max()), '\n')

# frequency distribution
print('\n ---------- Frequency Distribution for qualitative variables ---------- \n')
gender_freq = df.Gender.value_counts()
gender_percent = df.Gender.value_counts(normalize=True)
dist_freq_gender = pd.DataFrame({'Frequency': gender_freq, 'Percentage': gender_percent})
dist_freq_gender = dist_freq_gender.rename(index={0: 'Male', 1: 'Female'})
print('>>>> Gender Distribution Frequency <<<<')
print(dist_freq_gender, '\n')

gender_vs_color = pd.crosstab(index=df.Gender, columns=df.Color)
gender_vs_color = gender_vs_color.rename(index=gender, columns=color)
print('>>>>>> Gender vs Color Distribution Frequency <<<<<<')
print(gender_vs_color, '\n')

average_income = pd.crosstab(index=df.Gender, columns=df.Color, aggfunc='mean', values=df.Income)
average_income = average_income.rename(index=gender, columns=color)
print('>>>>>>>> Gender vs Color Average Income <<<<<<<<')
print(average_income, '\n')

# going from a continuous variable to a categorical variable
income_bins = [df.Income.min(), 1576, 3152, 7880, 15760, df.Income.max()]
income_labels = ['E', 'D', 'C', 'B', 'A']

categorical_income_freq = pd.cut(x=df.Income, bins=income_bins, labels=income_labels, include_lowest=True).value_counts()
print('----- Frequency Distribution for a quantitative continuous variable ----- \n')

categorical_income_percent = pd.cut(x=df.Income, bins=income_bins, labels=income_labels, include_lowest=True).value_counts(normalize=True)
categorical_income_complete = pd.DataFrame({'Frequency': categorical_income_freq, 'Percent (%)': categorical_income_percent*100})
print('Categorical Income Groups')
print(categorical_income_complete, '\n')

# using Sturges' Rule for applying a fixed amplitude
n = df.shape[0] # number of elements
k = 1 + ((10/3)*np.log10(n)) # Sturges Rule
k = int(k.round())

freq = pd.cut(x=df.Income, bins=k, include_lowest=True).value_counts(sort=False)
percent = pd.cut(x=df.Income, bins=k, include_lowest=True).value_counts(normalize=True, sort=False)
dist_freq_fixed_amplitude = pd.DataFrame({'Frequency': freq, 'Percent (%)': percent*100})

print("Sturges' Rule Categorical Income Groups")
print(dist_freq_fixed_amplitude, '\n')

