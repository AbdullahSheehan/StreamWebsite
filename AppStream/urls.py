from django.urls import path
from AppStream import views

app_name = 'AppStream'

urlpatterns = [
    path('',views.index, name='index'),
    path('categories/<pk>/', views.categories, name='category'),
    path('video/<pk>/', views.videoview, name='details'),
]