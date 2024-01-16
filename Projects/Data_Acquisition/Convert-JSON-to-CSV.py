import csv
import requests

url = "https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36"
r = requests.get(url)

r_json = r.json()

with open("./Projects/Data_Acquisition/Data/commute_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(r_json)