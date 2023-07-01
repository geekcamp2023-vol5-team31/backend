from django.urls import path
from . import views

urlpatterns = [
    path('create_event/', views.create_event, name='create_event'),
    path('get_events/', views.get_events, name='get_events'),
    path('get_event_detail/<int:event_id>/', views.get_event_detail, name='get_event_detail'),
    path('event_update/<int:event_id>/', views.event_update, name='event_update'),

    path('csrf_token/', views.csrf_token, name="csrf_token")
]