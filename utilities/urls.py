from django.urls import path

from . import views

app_name = 'utilities'

urlpatterns = [
    # path('', views.UtilityListView.as_view(), name='index'),
    path('', views.utility_list, name='utility_list'),
    # path('<int:pk>/', views.UtilityDetailView.as_view(), name='detail'),
    path('<slug:slug>/', views.UtilityDetailView.as_view(), name='detail')
]
