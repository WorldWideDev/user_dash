from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from views import Register, Show, Login, Logout, Dash, Edit, Delete, CreateMessage, CreateComment

urlpatterns = [
    url(r'^$', Register.as_view(), name='register'),
    url(r'^login$', Login.as_view(), name='login'),
    url(r'^logout$', Logout.as_view(), name='logout'),
    url(r'^dashboard$', Dash.as_view(), name='dashboard'),
    url(r'^users/edit/(?P<pk>\d+)', Edit.as_view(), name='edit'),
    # url(r'^users/delete/(?P<pk>\d+)', Delete.as_view(), name='delete'),
    url(r'^users/delete', Delete.as_view(), name='delete'),
    url(r'^users/(?P<pk>\d+)', Show.as_view(), name='show'),
    url(r'^message/create/(?P<pk>\d+)', CreateMessage.as_view(), name='create_message'),
    url(r'^comment/create/(?P<pk>\d+)', CreateComment.as_view(), name='create_comment'),
]
