#定义learning_logs的URL模式
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles

from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name='learning_logs'


urlpatterns = [
    # 主页
    #代码(?P<topic_id>\d+)捕获一个数字值并将其存储在topic_id中
    path("", views.index, name="index"),
    path("topics/", views.topics, name="topics"),
	#path("videos/", views.videos, name="videos"),
    path("topics/(?P<topic_id>\d+)/", views.topic, name="topic"),
    
    path("new_topic/", views.new_topic, name="new_topic"),

    path("new_entry/(?P<topic_id>\d+)/", views.new_entry, name="new_entry"),
    
    path("edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),
    #path("super/", views.map, name="map"),
    path("shop", views.shop, name="shop"),
    path("confirmation", views.confirmation, name="confirmation"),


    #测试ajax用
    path('update', views.update, name="update"),
    path('data_fresh/', views.data_fresh, name="data_fresh"),
    path("data/<int:id>/",views.data, name="data"),




    #
    # 通过构造的url传递数据，其url接口形式如下： http://127.0.0.1:8000/deal_data/?type=china&comment=niurou&price=5&amount=7
    # 在读取数据的时候，采用方法，p1 = request.GET.get('p1')，即可得到p1的数据
    path("deal_data/",views.deal_data, name="deal_data"),
    path("shou_yin/",views.shou_yin, name="shou_yin"),
    path("jiesuan/",views.jiesuan, name="jiesuan"),
]

#设置静态文件路径
urlpatterns += staticfiles_urlpatterns()
