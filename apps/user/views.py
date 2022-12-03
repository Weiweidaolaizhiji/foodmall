from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout

from django.views import View
from .forms import LoginForm


class LogoutView(View):
    def get(self, request,*args,**kwargs):
        if request.user.is_authenticated:
            logout(request)
            return HttpResponseRedirect(reverse('login'))
        return render(request,'login.html')


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'index.html')
        else:
            return render(request,'login.html')

    def post(self, request):
        username = request.POST.get('user')
        password = request.POST.get('pwd') #12345678
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return render(request,'index.html')
            else:
                return render(request,'login.html',{'msg':'您的账号密码有误，清重新输入！！！'})
        print(login_form.errors)
        return render(request,'login.html',{'login_form':login_form})


class RegisterView(View):
    def get(self, request):
        return render(request, 'reg.html')
