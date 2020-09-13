# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

COLUMNS = ['first_name', 'middle_name', 'last_name', 'birth_date', 'birth_place', 'profession', 'languages', 'political_party', 'email_address']


class ParlimentSpiderPipeline:
    def __init__(self):
        self.conn = sqlite3.connect('C:/Users/Lenovo/PycharmProjects/scrapy_spider/rest_api/db.sqlite3')
        self.cursor = self.conn.cursor()

    def insert_one(self, item):
        sql = f'INSERT INTO parliment({",".join(COLUMNS)}) VALUES({",".join(["?" for _ in range(len(COLUMNS))])})'
        self.cursor.execute(sql, (item['first_name'],
                                  item['middle_name'],
                                  item['last_name'],
                                  item['birth_date'],
                                  item['birth_place'],
                                  item['profession'],
                                  item['languages'],
                                  item['political_party'],
                                  item['email_address']))
        self.conn.commit()

    def process_item(self, item, spider):
        self.insert_one(item)
        return item
