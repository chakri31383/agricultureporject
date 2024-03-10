from django.contrib import admin
from django.urls import path

from .middlewares.auth import auth_middleware
from .views import additems, Signup, Login, logout, add_product, store


urlpatterns = [
    path('store', store, name='store'),

    path('additems', additems, name='additems'),
    path('add_product', add_product, name='add_product'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),


]