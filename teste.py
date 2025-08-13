import requests

headers = {
    "Authorization": "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzIiwiZXhwIjoxNzU0NDg1MzUzfQ.6grUB-c9naq7bHQ1DvQW3VYzGgQ1RKM3agwRTFJXmoU"
}

requisicao = requests.get("http://127.0.0.1:8000/auth/refresh", headers=headers)
print(requisicao)
print(requisicao.json())