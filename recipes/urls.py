#recipes/urls.py

from django.urls import path

from . import views

#what endpoints/paths exist and connect to the funtion
urlpatterns = [
    path('',views.recipe_list, name="recipe_list")
]