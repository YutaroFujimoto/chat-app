from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

#トップページを表示する処理
class HomeView(TemplateView):
    template_name = 'home.html'

#会員登録ページに関する処理
class UserCreateView(CreateView):
    template_name = 'authtest/user_create.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

# Create your views here.
def home(request):
    return render(request, 'authtest/home.html')