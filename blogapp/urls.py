from . import views
from django.urls import path

urlpatterns = [
    path('',views.home),
    path('contactus/',views.contactus),
    path('aboutus/',views.aboutus),
    path('login/',views.login),
    path('register/',views.register),
    path('post/<slug:url>',views.post),
    path('category/<slug:url>',views.category),
]