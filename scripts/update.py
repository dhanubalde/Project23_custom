import requests

get_update = int(input("What is your User Id? \n"))
endpoint = f"http://127.0.0.1:8000/user/{get_update}/update/"

create_data = {
    'name': 'dhanpot',
    'address': 'albany',
    'contact': 9201154542,
}

get_response = requests.put(endpoint, json=create_data)
print(get_response.json())