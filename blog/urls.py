from django.conf.urls import include, url
from views import Blog

from rest_framework import routers

from views import BlogViewSet

router = routers.DefaultRouter()
router.register(r'blog', BlogViewSet)

urlpatterns = [
    url(r'^$', Blog.as_view(), name='blog'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]