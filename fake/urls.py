
from django.urls import path, include
from .views import HomeView, TestCreate, TestDelete, TestUpdate, export_csv, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', HomeView.as_view(), name='home'),
    path('create/', TestCreate.as_view(), name='create'),
    path('delete/<int:pk>/', TestDelete.as_view(), name='delete'),
    path('update/<int:pk>/', TestUpdate.as_view(), name='update'),
    path('export_csv/', export_csv, name='export_csv'),
]
