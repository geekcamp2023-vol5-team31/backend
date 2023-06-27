from . import views
from django.urls import path

urlpatterns = [
    path('event_list/', views.event_list, name='event_list'),
    path('event_detail', views.event_detail, name='event_detail')
]