from .import views
from django.urls import path

app_name = "accounts"

urlpatterns = [
    path('join/',views.join,name='join'),
    path('signin/',views.SigninView.as_view(),name='signin'),
]