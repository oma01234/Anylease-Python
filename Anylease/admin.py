from django.contrib import admin
from .models import Items, User, Client, Customer

# Register your models here.
admin.site.register(Items)
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Customer)
