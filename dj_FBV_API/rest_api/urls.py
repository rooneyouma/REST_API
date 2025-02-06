from django.urls import path 
from . import views

urlpatterns = [
    path('api/Items/', views.ItemList, name='ItemList'),
    path('api/Items/<int:id>', views.ItemDetail, name='ItemDetail'),

]