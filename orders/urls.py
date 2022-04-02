from django.urls import path
from . import views

urlpatterns = [
   path('', views.OrderCreateListView.as_view(), name='orders')
]