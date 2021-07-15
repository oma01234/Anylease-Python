from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('home/', Home.as_view(), name='home'),
    path('post/', HomeView.as_view(), name='home1'),
    path('lender/', LenderView.as_view(), name='lender'),
    path('register/', views.register, name='register'),
    path('register/client_register/', ClientRegister.as_view(), name='client_register'),
    path('register/customer_register/', CustomerRegister.as_view(), name='customer_register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('client_page/', ClientPageView.as_view(), name='client_page'),
    path('customer_page/', CustomerPageView.as_view(), name='customer_page'),
    path('faq/', FaqView.as_view(), name='faq'),
    path('about/', AboutView.as_view(), name='about'),
    path('details/', DetailsView.as_view(), name='details'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('notify/', NotifyView.as_view(), name='notify'),
    path('messages/', MessageView.as_view(), name='messages'),

]

