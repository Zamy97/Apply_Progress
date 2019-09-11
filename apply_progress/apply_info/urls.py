from django.urls import path

from . import views

app_name = 'apply_info'
urlpatterns = [
    path('', views.index, name='index'),
]
