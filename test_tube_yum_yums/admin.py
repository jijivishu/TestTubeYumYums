# TODO: Add comments

# Django-based imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Internal imports
from .models import User, CBC, VitMin, CBCStat, VitMinStat, Range


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'dob', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_superuser',)
    readonly_fields = ('email',)
    
admin.site.register(User, CustomUserAdmin)
admin.site.register(CBC)
admin.site.register(VitMin)
admin.site.register(Range)
admin.site.register(CBCStat)
admin.site.register(VitMinStat)