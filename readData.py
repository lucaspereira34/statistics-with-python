# import pandas library
import pandas as pd

# read the file and store it in 'file' dataframe
file = pd.read_csv('PES2015.txt', header=None)

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

# create 'data' dataframe only with registers from people of reference
data = df.loc[df['Status_in_residence']=='1']

# drop 'Status_in_residence' column since we are considering only one value
data = data.drop(columns='Status_in_residence')

# drop invalids 'Income' values
data = data.loc[(data['Income']!='999999999999') & (data['Income']!='            ')]

# convert numeric data to numeric format
data['Income'] = pd.to_numeric(data['Income'])
data['Age'] = pd.to_numeric(data['Age'])

# create .csv file with 'data' dataframe
data.to_csv('data.csv', index=False)