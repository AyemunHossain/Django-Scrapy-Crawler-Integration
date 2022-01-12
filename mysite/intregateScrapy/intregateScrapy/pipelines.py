# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class LinkSpiderPipline(object):
    def process_item(self, item, spider):
        model_class = getattr(item, 'django_model')
        
        obj = model_class.objects.create(title=str(item['title']).replace('"', ""), author=item['author'], tag=item['tag'])
        
        obj.save()
        return item
