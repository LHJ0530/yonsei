from django.urls import path
from.import views
app_name = 'product'

urlpatterns = [
    path('', views.mainpage),
    path('loginsign/', views.loginsign, name='loginsign'),
    path('chatting/', views.chatting, name='chatting'),
    path('sign/', views.sign, name='sign'),
    path('todaynews/', views.todaynews, name='todaynews'),
    path('likecheck/', views.likecheck, name='likecheck'),
    
   
]