from django.shortcuts import render
from django.views.generic import TemplateView

class PythonQuiz(TemplateView):
    template_name = 'python_quiz/static/templates/python_quiz.html'

    def get(self, request):
        return render(request, self.template_name)