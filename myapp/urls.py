from django.urls import path
from . import views

urlpatterns = [
    #追加分
    path('get_events/', views.get_events, name='get_events'),
    path('get_event_detail/', views.get_event_detail, name='get_event_detail'),
    path('event_update/', views.event_update, name='event_update'),
    path('csrf_token/', views.csrf_token, name="csrf_token")
]