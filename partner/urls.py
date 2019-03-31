from django.conf.urls import url, include
from .views import (
    index,
    edit_info,
    signup, login, logout, #auth
    menu, menu_add,
)

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^edit/$', edit_info, name='edit_info'),
    url(r'^menu/$', menu, name='menu'),
    url(r'^menu/add/$', menu_add, name='menu_add'),
]