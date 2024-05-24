import pandas as pd

# Load the data
df = pd.read_csv('Report_Card_Growth_for_2022-23.csv')

# Filter rows where OrganizationLevel is 'State'
state_df = df[df['OrganizationLevel'] == 'State']

# Columns to keep
columns_to_keep = [
    'OrganizationLevel', 'StudentGroup', 'GradeLevel', 'Subject', 
    'MedianSGP', 'StudentCount', 'NumberLowGrowth', 'NumberTypicalGrowth', 
    'NumberHighGrowth', 'PercentLowGrowth', 'PercentTypicalGrowth', 
    'PercentHighGrowth'
]

# Extracting necessary columns
cleaned_df = state_df[columns_to_keep]

# Remove duplicate rows
cleaned_df.drop_duplicates(inplace=True)

# Save to a new CSV file
cleaned_df.to_csv('state_table.csv', index=False)
