from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from.import views

urlpatterns=[

    url('login/$', views.logon,name='logon'),
    url('log/$',views.login,name='login'),
    url('edit_profile/$', views.edit_profile, name='edit_profile'),
    # url('^confirmation',views.confirmation,name='confirmation'),
    path('', views.home,name='home'),
    url('register/$',views.UserFormView.as_view(),name='register'),


]