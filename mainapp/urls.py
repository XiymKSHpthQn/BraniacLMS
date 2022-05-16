from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.HelloWorldView.as_view()),
    path("<str:word>/", views.check_kwargs),
]