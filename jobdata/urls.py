from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_data, name='home'),
    path('data_list/', views.data_list, name='data_list'),
]



