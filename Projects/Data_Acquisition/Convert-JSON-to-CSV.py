# Import necessary libraries
import csv
import requests

# Define the URL for the API endpoint
url = "https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36"

# Send a GET request to the API endpoint
r = requests.get(url)

# Convert the response to JSON
r_json = r.json()

# Open a CSV file in write mode
with open("./Projects/Data_Acquisition/Data/commute_data.csv", mode="w", newline="") as file:
    # Create a CSV writer
    writer = csv.writer(file)
    # Write the JSON data to the CSV file
    writer.writerows(r_json)