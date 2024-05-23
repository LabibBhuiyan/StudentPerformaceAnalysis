import pandas as pd

# Load the data
df = pd.read_csv('state_table.csv')

# Filter out rows with missing values in the 'StudentCount' and 'GradeLevel' column
df = df.dropna(subset=['GradeLevel', 'StudentCount'])

# Filter out rows where 'GradeLevel' is 'AddedRow'
df = df[df['GradeLevel'] != 'AddedRow']

# Convert percentage columns to percentage format
percentage_columns = ['PercentLowGrowth', 'PercentTypicalGrowth', 'PercentHighGrowth']
for col in percentage_columns:
    df[col] = (df[col] * 100).map('{:.2f}%'.format)
    
# Save the cleaned DataFrame to a new CSV file
df.to_csv('cleaned_state_table.csv', index=False)
