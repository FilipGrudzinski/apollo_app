from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    url(r'^app/?$', views.index, name='base'),
    url(r'^$', login, {'template_name': 'recrut/login.html'}, name='login'),
    url(r'^material/?$', views.material, name='material'),
    url(r'^details/(?P<company_id>[0-9]+)$', views.details,
        name='company_details'),
]
