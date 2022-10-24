import requests

endpoint = "http://localhost:8000/api/products/1/"


get_response = requests.get(endpoint, json = {"product_id": 123})
print(get_response.json())#print the response in JSON format