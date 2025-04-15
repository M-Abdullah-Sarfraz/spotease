from django.urls import path
from . import views

urlpatterns = [
    path('choose_category/', views.choose_category, name='choose_category'),
    path('post/<str:category>/', views.post_ad, name='post_ad'),
]
