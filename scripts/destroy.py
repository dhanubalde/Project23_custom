import requests

get_delete = int(input("What is your User ID?\n"))
endpoint = f"http://127.0.0.1:8000/user/{get_delete}/delete/"

get_response = requests.delete(endpoint)
print(get_response.json())