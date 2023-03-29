from django.urls import path
from . import views



urlpatterns = [
    path('', views.ClassListView.as_view(), name='class_list'),
    path('<int:pk>', views.ClassDetailView.as_view(), name='class_detail'),
    path('<slug:slug>/', views.ClassDetailView.as_view(), name='class_detail_test'),
]