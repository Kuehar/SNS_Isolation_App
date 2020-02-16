from .import views
from django.urls import path


urlpatterns = [
    path('top/',views.TopView,name='top'),
]