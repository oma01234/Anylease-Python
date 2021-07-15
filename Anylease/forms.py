from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Items, Customer, Client, User
from django.db import transaction


class UserForm(forms.ModelForm):

    class Meta:
        model = Items
        fields = ['Item_Category', 'Item_Name', 'Item_Amount', 'Image']


class CustomerSignUp(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    location = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone_number = self.cleaned_data.get('phone_number')
        customer.location = self.cleaned_data.get('location')
        customer.save()
        return customer


class ClientSignUp(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    designation = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        client = Client.objects.create(user=user)
        client.phone_number = self.cleaned_data.get('phone_number')
        client.designation = self.cleaned_data.get('designation')
        client.save()
        return client
