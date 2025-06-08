from django.urls import path
from . import views


urlpatterns = [
    path('', views.t101, name='t101'),
]
