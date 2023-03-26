from django.urls import path
from informationhub import views

app_name = 'informationhub'

urlpatterns = [
path('', views.homepage, name='homepage'),
path('portfolio', views.portfolio, name='portfolio'),
path('about', views.about, name='about'),
]
