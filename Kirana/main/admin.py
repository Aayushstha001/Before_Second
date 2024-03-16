from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

admin.site.register(Category)
admin.site.register(Product)

class InfoInline(admin.StackedInline):
    model = Info

class UserAdmin(admin.ModelAdmin):
    model = User
    field = '__all__'
    inlines = [InfoInline]

admin.site.unregister(User)

admin.site.register(User, UserAdmin)