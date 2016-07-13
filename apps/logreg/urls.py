from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from views import Register, Success, Login, Logout

urlpatterns = [
    url(r'^$', Register.as_view(), name='register'),
    url(r'^login$', Login.as_view(), name='login'),
    url(r'^logout$', Logout.as_view(), name='logout'),
    url(r'^success$', login_required(Success.as_view(), login_url='/login'), name='success'),
]