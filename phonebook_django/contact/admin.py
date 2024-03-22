from django.contrib import admin
from django.contrib.admin import register
from .models import Information, Phone
# Register your models here.


@register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'address')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('id', 'address')


@register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number')


