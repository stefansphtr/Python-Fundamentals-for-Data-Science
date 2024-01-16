import requests
# r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E&for=state:*')

# # Access data as JSON string
# print(f"This is the results if the data turns into a string using .text: \n {r.text} \n")

# # Access decoded JSON data as Python object
# print(f"This is the results if the data turns into the Python object using .json(): \n {r.json()}")
url = 'https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36'
r = requests.get(url)

r_text = r.text

print(f"This is the results of the data from all countries within the state of New York using .text: \n {r_text}")

r_json = r.json()

print(f"\n This is the results of the data from all countries within the state of New York using .json(): \n {r_json} \n")

"""
Explanation:
The `.text` attribute in the `requests` library in Python returns the response content in Unicode format.
It's a raw string of the response body.

On the other hand, the `.json()` method returns a Python dictionary or list that represents the parsed JSON data
from the response body. 

The advantage of using `.json()` over `.text` is that `.json()` converts the JSON response into a Python data structure
(like a dictionary or a list), which makes it easier to interact with. You can access values in the response 
by key or index, iterate over elements, and use other Python data structure operations.

For example, 
if the response is `{"key": "value"}`, with `.text` you would get a string `'{ "key": "value" }'`, 
but with `.json()` you would get a Python dictionary `{'key': 'value'}`. Now you can access the value 
with `response['key']`, which you couldn't do with the string.

So, if you're working with JSON data, it's generally more convenient to use `.json()`.
"""

# The difference between the two outputs is the type of data structure they represent.

first_information = r_text[0]
print(f"This is the first information from the .text: \n {first_information} \n")
# Output: [ 

first_information = r_json[0]
print(f"This is the first information from the .json(): \n {first_information}")
# Output: ['NAME', 'B08303_001E', 'B08303_013E', 'state', 'county']

"""
So, by using .json(), you can easily access, manipulate, 
and analyze the data using Python's built-in list and dictionary operations.
"""