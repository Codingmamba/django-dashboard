from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^main$', views.index, name='index'),

    url(r'^main/register$', views.register, name='register'),
    url(r'^main/login$', views.login, name='login'),
    url(r'^main/logout$', views.logout_view, name='logout'),

    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^add/(?P<id>\d+)$', views.addList, name='addList'),
    url(r'^main/(?P<id>\d+)/delete$', views.delete, name='delete'),

    url(r'^wish_list/create$', views.create, name="list_create"),
    url(r'^item/create$', views.formCreate, name='new_product'),
    url(r'^wish_list/(?P<id>\d+)$', views.listDisplay, name="product_display"),
]
