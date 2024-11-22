from django.urls import path
from . import views

urlpatterns = [
    # int:id here will be the ID of the to do list (counts from 1)
    path("<int:id>", views.index, name="index"),
]
