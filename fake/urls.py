
from django.urls import path, include
from .views import HomeView, TestCreate, TestDelete, TestUpdate, export_csv

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', TestCreate.as_view(), name='create'),
    path('delete/<int:pk>/', TestDelete.as_view(), name='delete'),
    path('update/<int:pk>/', TestUpdate.as_view(), name='update'),
    path('export_csv/', export_csv, name='export_csv'),
]
