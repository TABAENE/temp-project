from django.shortcuts import render
from django.views.generic import TemplateView
from serializers import BlogSerializer
from rest_framework import viewsets

from models import BlogModel


class Blog(TemplateView):
    template_name = 'static/templates/_blog.html'

    def get(self, request):
        return render(request, self.template_name)

class BlogViewSet(viewsets.ModelViewSet):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer