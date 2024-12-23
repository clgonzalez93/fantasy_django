from django.urls import path
from . import views

urlpatterns = [
    # int:id here will be the ID of the to do list (counts from 1)
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
]
