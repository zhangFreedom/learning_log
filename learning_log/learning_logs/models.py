from django.db import models

from django.contrib import admin


from django.contrib.auth.models import User

# Create your models here.
'''

#CharField表示由字符和文本组成的数据，参数为预留数据空间。
    #text主要用来存储数据
    DateTimeField用于记录时间和日期，
    auto_now_add=True表示创建新主题时，Django自动将这个属性设为当前日期和时间
    熟悉模型使用字段，参考https://docs.djangoproject.com/en/1.8/ref/models/fields/
'''


class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    # 由于和“主题”是多对一的关系，所以“主题”是“条目”的外键
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """返回模型的字符串表示"""
        # 由于条目包含的文本可能很长，只显示前50个字符
        return self.text[:50] + "..."

		
#上传图片的模型类，name需要在执行数据库迁移时候选择1，进行创建，输入  ‘name’  即可		
class Img(models.Model):
    img = models.ImageField(upload_to='media')
    name =models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)
    
    #def __str__(self):
        #return self.pic


