from django.urls import path

from . import views

urlpatterns = [
    # path('', views.UtilityListView.as_view(), name='index'),
    path('', views.utility_list, name='utility_list'),
    path('<int:pk>/', views.UtilityDetailView.as_view(), name='detail')
]
