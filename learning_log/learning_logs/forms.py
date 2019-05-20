from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:#告诉django根据那个模型创建表单，以及在表单中包含哪些字段
        model =Topic#创建表单
        fields=['text']
        labels={'text':''}#不为该字段生成标签
        
class EntryForm(forms.ModelForm):
    class Meta:
        
        model =Entry
        fields=['text']
        labels={'text':''}#不为该字段生成标签
        widgets={'text':forms.Textarea(attrs={'cols':80})}
        #表单元素，如单行文本框或多行文本区域P387


