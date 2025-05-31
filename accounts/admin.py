from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('اطلاعات اضافی', {
            'fields': (
                'role',
                'phone_number',
                'gender',
                'profile_picture',
                'created_at',
                'updated_at',
            )
        }),
    )
    readonly_fields = ['created_at', 'updated_at', 'profile_preview']
    list_display = ['username', 'email', 'role', 'phone_number', 'profile_preview']

    def profile_preview(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" width="40" height="40" style="border-radius:50%;" />', obj.profile_picture.url)
        return 'ندارد'
    profile_preview.short_description = 'پروفایل'

