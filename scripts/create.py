import requests


endpoint = "http://127.0.0.1:8000/user/"

create_data = {
    'name': 'dhanpot',
    'address': 'albany',
    'contact': 9201154542,
}

get_response = requests.post(endpoint, json=create_data)
print(get_response.json())