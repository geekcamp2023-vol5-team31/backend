from django.urls import path
from . import views

urlpatterns = [
    path('event_list/', views.event_list, name='event_list'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'), 
]