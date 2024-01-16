# Import the pandas library
import pandas as pd

# Read the CSV file into a DataFrame
commute_df = pd.read_csv("./Projects/Data_Acquisition/Data/commute_data.csv")

# Print the first 5 rows of the DataFrame
print(commute_df.head())

"""
Rename the columns of the DataFrame: 
- "name" for the name of the county
- "total_commuters" for the total number of commuters (B08303_001E)
- "long_commute_90min_plus" for the number of commuters who travel 90 or more minutes (B08303_013E)
- "state" for the state code
- "county" for the county code
"""
commute_df.columns = ["name", "total_commuters", "long_commute_90min_plus", "state", "county"]

# Print the first 5 rows of the DataFrame after renaming the columns
print(commute_df.head())