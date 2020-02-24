from .import views
from django.urls import path

app_name = 'top'

urlpatterns = [
    path('index/',views.TopView.as_view(),name='index'),
]