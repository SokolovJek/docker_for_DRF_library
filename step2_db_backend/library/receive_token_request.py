import requests


response = requests.post('http://127.0.0.1:8000/api-token-auth/', data={'username': 'user1', 'password': 'geekshop'})
print(response.status_code)     # 200
print(response.json())         # {'token': 'f8004d8411aea2859e4e104fcffacd4272dea8fa'}
