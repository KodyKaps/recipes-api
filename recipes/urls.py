#recipes/urls.py

from django.urls import path

from . import views

#what endpoints/paths exist and connect to the funtion
urlpatterns = [
    path('landing',views.landing_page, name="landing_page"),
    path('',views.recipe_list, name="recipe_list"),
    path('reviews', views.reviews, name='reviews')
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout')
]