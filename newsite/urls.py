from django.conf.urls import include, url
from django.contrib import admin
from home.views import Home

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Home.as_view()),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^python_quiz/', include('quiz.python_quiz.urls')),
]
