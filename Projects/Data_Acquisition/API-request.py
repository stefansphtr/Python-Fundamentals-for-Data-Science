import requests
# r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E&for=state:*')

# # Access data as JSON string
# print(f"This is the results if the data turns into a string using .text: \n {r.text} \n")

# # Access decoded JSON data as Python object
# print(f"This is the results if the data turns into the Python object using .json(): \n {r.json()}")

r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36')

r_text = r.text

print(f"This is the results of the data from all countries within the state of New York using .text: \n {r_text}")

r_json = r.json()

print(f"\n This is the results of the data from all countries within the state of New York using .json(): \n {r_json}")

