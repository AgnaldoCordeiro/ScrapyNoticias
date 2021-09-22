# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


class NoticiasPipeline:
   def __init__(self):
        client = pymongo.MongoClient("mongodb+srv://agnaldocordeiro:ag5323896@cluster0.kytmu.mongodb.net/ScrapyNoticias?retryWrites=true&w=majority")
        self.conn = client
        db = client.test
        db = self.conn['ScrapyNoticias']
        self.collection = db['noticias_tb']
        
   

   def process_item(self, item, spider):
        self.collection.insert(dict(item))      
        return item







"""chave privada mongodb api 9ff19e83-00ed-4506-8404-5d6bfdf3753c"""

