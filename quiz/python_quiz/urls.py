from django.conf.urls import url
from views import PythonQuiz

urlpatterns = [
    url(r'^$', PythonQuiz.as_view(), name='python_quiz'),
]
