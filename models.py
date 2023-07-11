import requests
import json
import os

# URL to send the POST request to
url = 'https://api.openai.com/v1/models'

# Data to send in the POST request
# data = {
#     'key1': 'value1',
#     'key2': 'value2'
# }

apikey = os.getenv('OPENAI_API_KEY')

# The headers for the request
headers = {
    'Authorization': f'Bearer {apikey}',
    'Content-Type': 'application/json'
}

# Send the POST request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response as JSON
    response_json = response.json()
    models = []
    for i in range(0, len(response_json['data'])):
        item = response_json['data'][i]
        if item['object'] == 'model':
            models.append(str(item['id']))

    models = sorted(models)

    with open('results/models.txt', 'w') as f:     
        for i in range(0, len(models)):
            f.write(f"- {models[i]}\n")
    # Do something with the response
    # print(response_json)
else:
    print(f'Request failed with status code {response.status_code}')
    print(response.text)
