import requests

URL='http://127.0.0.1:8000/student/'
books=requests.get(url=URL)

print(books.json())
