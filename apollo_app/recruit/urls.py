from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    url(r'^app/?$', views.company, name='base'),
    url(r'^$', login, {'template_name': 'recruit/login.html'}, name='login'),
    url(r'^materials/?$', views.materials, name='material_view'),
    url(r'^company_assigned/(?P<company_id>[0-9]+)$', views.company_assigned,
        name='company_details'),
    url(r'^material_detail/(?P<_id>[0-9]+)$', views.material_detail,
        name='about_material'),
]
