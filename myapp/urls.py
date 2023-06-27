from . import views
from django.urls import path

urlpatterns = [
    path('data/', views.EventDetailsView.as_view(), name='data')
]