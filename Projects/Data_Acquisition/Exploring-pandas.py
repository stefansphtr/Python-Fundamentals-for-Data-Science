import pandas as pd

commute_df = pd.read_csv("./Projects/Data_Acquisition/Data/commute_data.csv")

print(commute_df.head())

commute_df.columns = ["name", "total_commuters", "long_commute_90min_plus", "state", "county"]
# total_commuters for "Total commuters count" (B08303_001E)
# long_commute_90min_plus for "The count for commuters who travel 90 or more minutes" (B08303_013E)

print(commute_df.head())

