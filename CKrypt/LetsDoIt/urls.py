from django.urls import path
from . import views

app_name = "LetsDoIt"
urlpatterns = [
    path("", views.index, name="index"),
    path("addtask", views.addtask, name = "addtask")
]