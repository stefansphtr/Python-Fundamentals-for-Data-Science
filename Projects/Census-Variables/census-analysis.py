# Import pandas with alias
import pandas as pd
import numpy as np

# Set pandas option to display all columns
pd.set_option('display.max_colwidth', None)

# Read in the census dataframe
census = pd.read_csv("./Projects/Census-Variables/data/census_data.csv", index_col=0)

print(census.head())

# Check the datatypes of each variable in the census dataframe
print(census.dtypes)

# List the changes needed from the dataframe
changes = ['first_name', 'last_name', 'birth_year', 'voted', 'string']

# Check the unique values in the higher_tax variable
# print(census['higher_tax'].unique())

# Check the unique values in the birth year variable
print(census.birth_year.unique())

# # Fill the missing value in the birth year with 1967
census['birth_year'] = census['birth_year'].replace('missing', '1967')

# # Change the data type of birthday_year to integer
census['birth_year'] = census['birth_year'].astype('int64')

# # Check the datatypes again
print(census.dtypes)

# # Find the average birth year of the respondends
avg_birth_year = round(census['birth_year'].mean())

print(f"The average birth year of the respondends is: {int(avg_birth_year)}")

# Convert the higher tax variable into categorical variable

census['higher_tax'] = pd.Categorical(
  census['higher_tax'], 
  ['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree'],
  ordered=True
)

census['higher_tax'] = census['higher_tax'].cat.codes

print(census['higher_tax'].unique())

census['higher_tax']

# Print out the median of the higher_tax variable
# print(census['higher_tax'].unique())
median_higher_tax = census['higher_tax'].median()
print(f"The median sentiments of the responded is: {median_higher_tax}")

# # Create new variable marital_codes by label encoding the marital_status

# # One-hot encode the marital_status
census = pd.get_dummies(census['marital_status'], prefix='status').astype('int64')

# Print out the head of the df
print(census.head())

# Create a new variable age_group which groups based on the birth year

# Calculate the age
census['age'] = 2024 - census['birth_year']

# Print the minimum age in the 'age' column
print(census['age'].min()) 

# Print the maximum age in the 'age' column
print(census['age'].max()) 

# Define the conditions for each age group
group_ages = [
    (census['age'] >= 46),  # Old-aged-adults: age 46 and above
    (census['age'] >= 31) & (census['age'] <= 45),  # Middle-aged-adults: age between 31 and 45
    (census['age'] >= 17) & (census['age'] <= 30)  # Young-adults: age between 17 and 30
]

# Define the category names for each age group
group_cat = ['Old-aged-adults', 'Middle-aged-adults', 'young-adults']

# Create a new column 'age_group' in the DataFrame by selecting the age group for each row
census['age_group'] = np.select(group_ages, group_cat)

# Print the first 5 rows of the 'age_group' column
print(census['age_group'].head())