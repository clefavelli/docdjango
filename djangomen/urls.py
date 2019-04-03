from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:board_id>/', views.distributor, name='distributor'),
]
