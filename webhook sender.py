import requests
import json

webhook_url = 'TON_WEBHOOK'

message_content = 'TON_MESSAGE'

payload = {
    'content': message_content
}
response = requests.post(webhook_url, json=payload)

if response.status_code == 204:
    print('Message parfaitement envoyé')
else:
    print(f'Le message n\'a pas été envoyé... : {response.status_code} {response.text}')
