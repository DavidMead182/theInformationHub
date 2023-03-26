from django.urls import path
from informationhub import views

app_name = 'informationhub'

urlpatterns = [
path('', views.homepage, name='homepage'),
]
