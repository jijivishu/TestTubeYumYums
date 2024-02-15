# Django based imports
from django.urls import path

# Internal imports
from . import views

# List of url patterns utilized by our app
urlpatterns = [
    # Landing page
    path('/', views.index, name="index"),

    # Authentication
    path('authenticate/', views.authenticate_view, name="authenticate"),

    # Analysis of most-recent test
    path('analysis/', views.analysis, name="analysis"),

    # Logout currently logged user
    path('logout/', views.logout_view, name="logout"),

    # Fetch JSON response contaiining list of countries (API)
    path('country_list/', views.country_list, name="country_list"),

    # Create, Update and Retrieve ranges (API)
    path('para_range/', views.para_range, name="para_range"),

    # Add new test values
    path('add/', views.add, name="add")
]
