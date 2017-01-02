from django.views.generic import TemplateView
from django.shortcuts import render
from forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.contrib.auth.models import User

class Login(TemplateView):

    template_name = 'login.html'

    def get(self,request):
        form = LoginForm()
        return render(request,self.template_name, {'form':form})

    def post(self,request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        form = LoginForm(request.POST)
        #context = RequestContext(request, {'form':form})
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        return render(request, self.template_name, {'form':form})

class Register(TemplateView):
    template_name = 'register.html'

    def get(self,request):
        form = RegisterForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(data['username'],data['email'], data['password'])
            user = authenticate(username=data['username'], password=data['password'])
            login(request, user)
            return render(request, 'index.html')
        return render(request,self.template_name,{'form':form})

class Logout(TemplateView):

    template_name = 'index.html'

    def get(self,request):
        logout(request)
        return render(request,self.template_name)