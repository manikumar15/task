from django.contrib import admin
from .models import Register,ProductData
from django.http import HttpResponse

admin.site.site_header = 'Login Admin'


class Registeradmin(admin.ModelAdmin):
    list_display = ('username','email','password')
    list_filter = ('username',)
    search_fields = ('username',)

admin.site.register(Register,Registeradmin)



class Productadmin(admin.ModelAdmin):
    list_display = ('id','name','role')

admin.site.register(ProductData, Productadmin)