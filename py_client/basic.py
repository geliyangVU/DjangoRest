import requests
# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org"
# endpoint = "https://httpbin.org/anything"
# endpoint = "https://localhost:8000/"
endpoint = "http://localhost:8000/api"


get_response = requests.get(endpoint, params={"abc": 123}, json = {"query": "hello world"})
# print(get_response.text)
# print(get_response.json())#print the response in JSON format
# print(get_response.json()['message'])#print the response.message

print(get_response.status_code)# print the status code for debugging purpose









