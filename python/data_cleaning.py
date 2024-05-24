import pandas as pd

# Load the data
df = pd.read_csv('../data/state_table.csv')

# Filter out rows with missing values in the 'StudentCount' and 'GradeLevel' column
df = df.dropna(subset=['GradeLevel', 'StudentCount'])

# Filter out rows where 'GradeLevel' is 'AddedRow'
df = df[df['GradeLevel'] != 'AddedRow']

# Sum up the percentages for growth rows
df['TotalPercentage'] = df[['PercentLowGrowth', 'PercentTypicalGrowth', 'PercentHighGrowth']].sum(axis=1)

# Filter out rows where 'TotalPercentage' is not equal to 1
df = df[df['TotalPercentage'] == 1]

# Sum up the number of students for growth rows
df['TotalStudents'] = df[['NumberLowGrowth', 'NumberTypicalGrowth', 'NumberHighGrowth']].sum(axis=1)

# Filter out rows where 'TotalStudents' is not equal to 'StudentCount'
df = df[df['TotalStudents'] != 'StudentCount']

# Delete 'TotalPercentage' and 'TotalStudents' attributes
df = df.drop(columns=['TotalPercentage', 'TotalStudents'])

# Convert percentage columns to percentage format
percentage_columns = ['PercentLowGrowth', 'PercentTypicalGrowth', 'PercentHighGrowth']
for col in percentage_columns:
    df[col] = (df[col] * 100).map('{:.2f}%'.format)

# Remove duplicates
df = df.drop_duplicates()

# Save the cleaned DataFrame to a new CSV file
df.to_csv('../data/cleaned_state_table.csv', index=False)
