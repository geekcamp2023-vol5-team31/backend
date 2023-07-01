from django.urls import path
from . import views

urlpatterns = [
    path('event_list/', views.event_list, name='event_list'),
    path('save_data/', views.save_data, name='save_data'), 
    path('csrf_token/', views.csrf_token, name="csrf_token")
]