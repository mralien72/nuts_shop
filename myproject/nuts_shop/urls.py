from django.urls import path
from .views import index

# app_name = 'nuts_shop'
urlpatterns = [
    path('', index, name='index'),
    ]