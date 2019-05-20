# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.contrib import staticfiles


from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
app_name = "users"
urlpatterns = [
  path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
  path('logout/', views.logout_view, name="logout"),
  path("register/", views.register, name="register"),
]

#设置静态文件路径
#urlpatterns += staticfiles_urlpatterns()