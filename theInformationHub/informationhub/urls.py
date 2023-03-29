from django.urls import path
from informationhub import views

app_name = 'informationhub'

urlpatterns = [
path('', views.homepage, name='homepage'),
path('portfolio', views.portfolio, name='portfolio'),
path('about', views.about, name='about'),
path('portfolio/myChatGla', views.myChatGla, name='myChatGla'),
path('portfolio/heartbeat', views.heartbeat, name='heartbeat'),
path('portfolio/thinformationhubsite', views.thinformationhubsite, name='thinformationhubsite'),
]
