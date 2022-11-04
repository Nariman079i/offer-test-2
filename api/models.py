from django.contrib import admin
from django.db.models import *

# Create your models here.


class Object(Model):

    name = CharField(max_length=50)
    age = IntegerField()
    description = TextField()
    cat_id = ForeignKey('Category', on_delete=CASCADE, null=True)


class Category(Model):
    title = CharField(max_length=30)
    priority = IntegerField()


admin.site.register(Category)
admin.site.register(Object)



