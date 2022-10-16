from django.contrib import admin
from .models import Company

# Register your models here.
class companyAdmin(admin.ModelAdmin):
    search_fields = ['subject']

#장고 화면사이트에 추가
admin.site.register(Company, companyAdmin)