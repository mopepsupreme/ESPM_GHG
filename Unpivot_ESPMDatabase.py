import pandas as pd

# Read in the CSV file
df = pd.read_csv('rawdata.csv')

# Split the Certification Years and Scores columns into lists of values and explode them
xd = pd.DataFrame({
    'Certification Years': df['Certification Years'].str.split(',').apply(pd.Series).stack(),
    'Score(s)': df['Score(s)'].str.split(',').apply(pd.Series).stack(),
}).reset_index(level=1, drop=True)

# Join the expanded columns back to the original DataFrame
df_expanded = df.drop(['Certification Years', 'Score(s)'], axis=1).join(xd)


# Write the expanded DataFrame to a new CSV file
df_expanded.to_csv('rawdata_unpivoted.csv', index=False)
