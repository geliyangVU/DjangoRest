import requests
endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org"

endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint)
print(get_response.text)
print(get_response.json())#print the response in JSON format
print(get_response.status_code)# print the status code for debugging purpose









