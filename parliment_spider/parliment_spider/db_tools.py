import sqlite3
import requests
import json

COLUMNS = ['birth_date', 'birth_place', 'profession', 'languages', 'political_party', 'email_address']
connection = sqlite3.connect('C:/Users/Lenovo/PycharmProjects/scrapy_spider/rest_api/db.sqlite3')
cursor = connection.cursor()

#cursor.execute(f'CREATE TABLE parliment ({", ".join([" ".join((name, "varchar")) for name in COLUMNS])})')
#cursor.execute(f'DROP TABLE parliment')


url = 'http://127.0.0.1:8000/list/'
headers = {'Authorization': 'Token a414577c12a52c860cdad995e85ea4dab5d34d96'}
response = requests.get(url, headers=headers)
json_response = json.loads(response.content)
print(json_response)

def select():
    selected_list = []