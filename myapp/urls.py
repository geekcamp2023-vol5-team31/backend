from django.urls import path
from . import views

urlpatterns = [
    #追加分
    path('get_events/', views.get_events, name='get_events'),
    path('get_event_detail/', views.get_event_detail, name='get_event_detail'),
    
    path('event_list/', views.event_list, name='event_list'),
    path('save_data/', views.save_data, name='save_data'), 
    path('csrf_token/', views.csrf_token, name="csrf_token")
]