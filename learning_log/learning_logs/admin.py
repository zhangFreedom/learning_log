from django.contrib import admin

# Register your models here.

from learning_logs.models import Topic,Entry,Img
admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Img)