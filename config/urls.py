from django.contrib import admin
from django.urls import path
from portfolio_app.views import post_view

urlpatterns = [
    path('home/', post_view, name='home'),
]