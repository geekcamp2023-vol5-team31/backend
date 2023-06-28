from django.urls import path
from . import views

urlpatterns = [
    path('save/<user_id>', views.save_data, name='save_data'),
    path('event_list/<user_id>', views.event_list, name='event_list'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'), 
]