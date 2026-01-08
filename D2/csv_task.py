import pandas as pd
import numpy as np

df = pd.read_csv('titanic.csv')

# Replacing / and " " with _
df.columns = df.columns.str.replace('/', '_')
df.columns = df.columns.str.replace(' ', '_')

print(df)

df.loc[df['Age'] < 18, 'Sex'] = 'child'

print(df)

#---------------------------------------

# Creating average fare based on sex
avg_male = df.query("Sex == 'male'")['Fare'].mean()
avg_female = df.query("Sex == 'female'")['Fare'].mean()
avg_child = df.query("Sex == 'child'")['Fare'].mean()

dataframe = {
    'Sex': ['male', 'female', 'child'],
    'Average_Fare': [avg_male, avg_female, avg_child]
}
df1 = pd.DataFrame(dataframe)

print(df1)

# Creating average fare based on sex and Pclass
avg_sex_pclass = df.groupby(['Sex', 'Pclass'])['Fare'].mean()
print(avg_sex_pclass)

# Creating average fare based on survived 
avg_survived = df.groupby('Survived')['Fare'].mean()
print(avg_survived)

# Creating 
df_male = df[df['Sex'] == 'male']
df_female = df[df['Sex'] == 'female']
df_child = df[df['Sex'] == 'child']

print(f"Male: {len(df_male)}")
print(f"Female: {len(df_female)}")
print(f"Child: {len(df_child)}")



condition = (df['Siblings_Spouses_Aboard'] > 0) | (df['Parents_Children_Aboard'] > 0)
subset_df = df.loc[condition, ['Pclass', 'Name', 'Age']]
print(subset_df.head())


condition2 = (df['Siblings_Spouses_Aboard'] > 0) & (df['Parents_Children_Aboard'] > 0)
subset2_df = df.loc[condition, ['Pclass', 'Name', 'Age', 'Fare']]
print(subset2_df.head())

ave_last = subset2_df['Fare'].mean()
print(ave_last)










