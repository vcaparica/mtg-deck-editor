from django.urls import path
from . import views

app_name = 'deckeditor'

urlpatterns = [
    path('', views.CardListView.as_view(), name='list'),
    path('<int:pk>/', views.CardDetailView.as_view(), name='detail'),
]