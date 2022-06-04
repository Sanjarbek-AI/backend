from django.contrib import admin

from user.models import UserModel


@admin.register(UserModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'created_date']
    list_filter = ['created_date']
    search_fields = ['first_name', 'last_name']
