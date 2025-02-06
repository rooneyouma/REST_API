from django.urls import path
from .views import ItemDetail, ItemList

urlpatterns = [
    path('api/Items/',ItemList.as_view(),name="ItemList"),
    path('api/Items/<int:id>/',ItemDetail.as_view(),name="ItemDetail")
]