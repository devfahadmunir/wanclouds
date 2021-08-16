from django.urls import path
from . import views
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from knox import views as knox_views

# knox is providing here the token functionality
# these are the urls patterns used for API paths
urlpatterns = [
    url(r'^APIregister/$', views.APIregister.as_view(), name='APIregister'),
    path('APIlogin/', views.APIlogin.as_view(), name='login'),
    path('APIlogout/', knox_views.LogoutView.as_view(), name='logout'),
    path('APIlogoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    url(r'^APIlist/$', views.APIlist.as_view(), name='APIlist'),
    url(r'^APIinsert/$', views.APIinsert.as_view(), name='APIinsert'),
    url(r'^APIupdate/$', views.APIupdate.as_view(), name='APIupdate'),
    url(r'^APIdelete/$', views.APIdelete.as_view(), name='APIdelete'),
    url(r'^APIsearch/$', views.APIsearch.as_view(), name='APIsearch'),
]
