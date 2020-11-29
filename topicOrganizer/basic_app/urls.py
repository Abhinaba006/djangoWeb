from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^create', views.create, name='create'),
    url(r'^view', views.view, name='view')
]
