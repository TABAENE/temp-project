from django.conf.urls import include, url
from views import Login, Register, Logout

urlpatterns = [
    url(r'^login/$', Login.as_view(), name='login_url'),
    url(r'^register/$', Register.as_view(), name='register_url'),
    url(r'^logout/$', Logout.as_view(), name='logout_url'),
]
