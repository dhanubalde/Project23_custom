import requests

get_retries = int(input("What is your User Id? \n"))

endpoint = f"http://127.0.0.1:8000/user/{get_retries}/"
get_response = requests.get(endpoint)
print(get_response.json())