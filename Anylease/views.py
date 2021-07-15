from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin


class HomeView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'user.is_client'
    login_url = '/login/'
    form_class = UserForm
    template_name = 'home1.html'
    model = Items
    success_url = reverse_lazy('home')


class Home(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Items
    template_name = 'home.html'


class LenderView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Items
    template_name = 'lender.html'


def register(request):
    return render(request, '../templates/register.html')


class CustomerRegister(CreateView):
    model = User
    form_class = CustomerSignUp
    template_name = '../templates/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class ClientRegister(CreateView):
    model = User
    form_class = ClientSignUp
    template_name = '../templates/client_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


# @login_required(login_url='/login/')
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_customer:
                    login(request, user)
                    return redirect('/customer_page')
                if user.is_client:
                    login(request, user)
                    return redirect('/client_page')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, '../templates/login.html',
                  context={'form': AuthenticationForm()})


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('index')


# class LogoutView(ListView):
#     model = Items
#     template_name = 'logout.html'
#     success_url = reverse_lazy('/login')


class IndexView(ListView):
    model = Items
    template_name = 'index.html'


class FaqView(ListView):
    model = Items
    template_name = 'faq.html'


class AboutView(ListView):
    model = Items
    template_name = 'about.html'


class DetailsView(ListView):
    model = Items
    template_name = 'details.html'


class SettingsView(ListView):
    model = Items
    template_name = 'settings.html'


class NotifyView(ListView):
    model = Items
    template_name = 'notify.html'


class MessageView(ListView):
    model = Items
    template_name = 'messages.html'


class CustomerPageView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    def test_func(self):
        return self.request.user.is_customer
    login_url = '/login/'
    model = Items
    template_name = 'customer_page.html'


class ClientPageView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    def test_func(self):
        return self.request.user.is_client
    login_url = '/login/'
    model = Items
    template_name = 'client_page.html'
