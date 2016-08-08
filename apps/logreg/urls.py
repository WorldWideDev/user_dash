from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from views import Register, Show, Login, Logout, Dash, Edit

urlpatterns = [
    url(r'^$', Register.as_view(), name='register'),
    url(r'^login$', Login.as_view(), name='login'),
    url(r'^logout$', Logout.as_view(), name='logout'),
    url(r'^dashboard$', Dash.as_view(), name='dashboard'),
    url(r'^users/edit/(?P<pk>\d+)', Edit.as_view(), name='edit'),
    url(r'^users/(?P<pk>\d+)', Show.as_view(), name='show')
]
