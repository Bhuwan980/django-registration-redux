from django.contrib import admin
from .models import Notice
# Register your models here.


class Admin(admin.ModelAdmin):
    list_display = ["subject",'date']
    search_fields = ['subject','message']
    list_per_page = 10
    list_filter = ['date']
    

admin.site.register(Notice,Admin)