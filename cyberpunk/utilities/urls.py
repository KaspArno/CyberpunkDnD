from django.urls import path

from . import views

urlpatterns = [
    path('', views.UtilityListView.as_view(), name='index'),
    path('<int:pk>/', views.UtilityDetailView.as_view(), name='detail'),
]
