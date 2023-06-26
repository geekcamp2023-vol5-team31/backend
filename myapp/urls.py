from . import views
from django.urls import path

urlpatterns = [
    #イベント作成
    path('create_event/', views.create_event, name='create_event'),
    
    #ログイン・ユーザ情報
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user/', views.user_view, name='user'),
]