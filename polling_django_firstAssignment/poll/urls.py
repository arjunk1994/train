from django.conf.urls import url

from.import views

urlpatterns=[
    url(r'^$',views.pol,name='pol'),
    url('Pollinternal$', views.Pollinternal,name='Pollinternal')
]