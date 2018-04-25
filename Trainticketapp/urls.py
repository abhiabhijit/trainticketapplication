"""Trainticketapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import signup,login_page,activate,index,logout,changepassword,forgotpassword
from updateprofile.views import update_profile
from realtimeinfo import views as apiview
from Bookingdetails import views as bookingviews

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^signup/$', signup, name='signup'),
    url(r'^signout/$', logout, name='signout'),
    url(r'login/$', login_page, name='login'),

    url(r'changepassword/$', changepassword, name='passwordreset'),

    url(r'forgotpassword/$', forgotpassword, name='forgotpassword'),

    url(r'^activate/(?P<uidb64>\d{1,})/$',
        activate, name='activate'),
url(r'home/$', index, name='home'),
url(r'/$', apiview.index, name='home_realtime'),
    url(r'profile/$', update_profile, name='profile'),
    url(r'carddetails/$', update_profile, name='CardDetails'),

    url(r'bookings/$', bookingviews.retrievebookings, name='bookings'),
    url(r'ticketdetails/(?P<pnr>\d{1,})/$', bookingviews.ticket_details, name='ticketdetails'),

]
