from django.db import models
from mongoengine import connect, Document, StringField, IntField, ListField


# connect('ganji', host='127.0.0.1', port=27017)


class GoodInfo(Document):
    item_url = StringField()
    price = IntField()
    sort = StringField()
    post_time = StringField()
    time = IntField()
    type = StringField()
    title = StringField()
    area = ListField(StringField())

    meta = {'collection': 'item_info'}

# for i in GoodInfo.objects[:1]:
#     print(i.price)
