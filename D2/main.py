import pandas as pd
import numpy as np

# Exercise 1 part 1 --------------------------------------------
dataframe1 = {
    'Name': ['Matti', 'Teppo', 'Jussi', 'Riku', 'Henri'],
    'Age': [35, 25, 45, 55, 28],
    'Score': [10.0, 12.1, np.nan, 16.3, np.nan]
}
df1 = pd.DataFrame(dataframe1)

print("DataFrame:")
print(df1)

# Indexing by name
df1.set_index('Name', inplace=True)

# Filtering ages above 25
greater_than_25 = df1[df1['Age'] > 25]
print("\nDataFrame > 25:")
print(greater_than_25)

# Changing Score datatype to float
df1['Score'] = df1['Score'].astype(float)
#print(df.dtypes)

# Grouping by age and calculating mean score for each age group
grouped_age = df1.groupby('Age')
mean_score = grouped_age['Score'].mean()

print("\nDataFrame grouped by age:")
print(mean_score)

# Replacing NULL values with a value 20.0
mean_score2 = df1['Score'].mean()
df1['Score'] = df1['Score'].fillna(mean_score2)

print("\nDataFrame without NULL values:")
print(df1)


# Exercise 1 part 2 --------------------------------------------
dataframe2 = {
    'Name': ['Marja', 'Liisa', 'Minna', 'Olivia', 'Julia'],
    'Age': [31, 21, 41, 51, 25],
    'Occupation': ['Project Manager', 'Product Manager', 'Sales Manager', 'RD Team Lead', 'DA Team Lead']
}
df2 = pd.DataFrame(dataframe2)

# Combining dataframes
combined_data = pd.concat([df1, df2])
print("\nDataFrames combined:")
print(combined_data)

dataframe3 = {
    'ID': ['101', '202', '303', '404', '505'],
    'Name': ['Marja', 'Liisa', 'Minna', 'Olivia', 'Julia'],
    'Age': [31, 21, 41, 51, 25]
}
df3 = pd.DataFrame(dataframe3)

dataframe4 = {
    'ID': ['101', '202', '303', '404', '505'],
    'Occupation': ['Project Manager', 'Product Manager', 'Sales Manager', 'RD Team Lead', 'DA Team Lead'],
    'Salary': [4500, 3500, 5500, 6500, 2500]
}
df4 = pd.DataFrame(dataframe4)

# Merging dataframes
merged_frames = pd.merge(df3, df4, on='ID')
print("\nDataFrames merged:")
print(merged_frames)


dataframe5 = {
    'Date': ['2025-12-20', '2025-12-21', '2025-12-22', '2025-12-23', '2025-12-24'],
    'ID': ['101', '202', '303', '404', '505']
}
df5 = pd.DataFrame(dataframe5)

# Changing string format to datetime object
df5['Date'] = pd.to_datetime(df5['Date'])

print(f"\n{df5.dtypes}")
print(f"\n{df5}")

# Renaming Date column to EventDate
renamed = df5.rename(columns={'Date':'EventDate'})
print(f"\n{renamed}")
# Renaming ID column to EventValue
renamed2 = df5.rename(columns={'ID':'EventValue'})
print(f"\n{renamed2}")


dataframe6 = {
    'ID': ['101', '101', '101', '404', '505']
}
df6 = pd.DataFrame(dataframe6)

print()
print("Unique values:")
uniq = df6['ID'].unique()
for value in uniq:
    print(value)















