import requests
# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org"
# endpoint = "https://httpbin.org/anything"
# endpoint = "https://localhost:8000/"
endpoint = "http://localhost:8000/api/"


get_response = requests.get(endpoint, json = {"product_id": 123})
# print(get_response.text)
print(get_response.json())#print the response in JSON format
# print(get_response.json()['message'])#print the response.message

# print(get_response.status_code)# print the status code for debugging purpose









