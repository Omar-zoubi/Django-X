from django.urls import path 
from .views import HomeListView, DetailsListView, CreateListView, UpdateListView, DeleteListView

urlpatterns = [
    path("", HomeListView.as_view(), name='list'),
    path("<int:pk>/", DetailsListView.as_view(), name='details'),
    path("create/", CreateListView.as_view(), name='create'),
    path("<int:pk>/update/", UpdateListView.as_view(), name="update"),
    path("<int:pk>/delete/", DeleteListView.as_view(), name="delete")
]