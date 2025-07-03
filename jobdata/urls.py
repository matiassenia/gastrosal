from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_data, name='upload_data'),
    path('data_list/', views.data_list, name='data_list'),
]



