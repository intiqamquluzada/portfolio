from django.urls import path
from portfolio.views import *

urlpatterns = [
    path("", home_view, name="home"),
    path("projects/", projects_view, name='projects'),

]
