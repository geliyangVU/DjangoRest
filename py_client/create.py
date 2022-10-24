import requests

endpoint = "http://localhost:8000/api/products/"
data = {
    "title": "title field",
    "price":100.05
}
get_response = requests.post(endpoint, json = data)
print(get_response.json())#print the response in JSON format