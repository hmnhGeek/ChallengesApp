from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    # the order here matters. First we want to check if month can be converted to integer
    # if not, then convert to string.
    path("<int:month>", views.index_by_int),
    path("<str:month>", views.index)
]