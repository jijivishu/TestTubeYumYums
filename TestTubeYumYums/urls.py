# Django based imports
from django.contrib import admin
from django.urls import path, include

# Internal imports
from . import views

# List of url patterns utilized by our app
urlpatterns = [
    # Landing page
    path('', views.index, name="index"),

    # Authentication
    path('authenticate', views.authenticate_view, name="authenticate"),

    # Analysis of most-recent test
    path('analysis', views.analysis, name="analysis"),

    # Logout currently logged user
    path('logout', views.logout_view, name="logout"),

    # Fetch JSON response contaiining list of countries (API)
    path('countryList', views.countryList, name="countryList"),

    # Create, Update and Retrieve ranges (API)
    path('paraRange', views.paraRange, name="paraRange"),

    # Add new test values
    path('add', views.add, name="add")
]
