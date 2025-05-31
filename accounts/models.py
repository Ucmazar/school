from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime



def profile_image_upload_path(instance, filename):
    today = datetime.today()
    return f'profile_image/{today.year}/{today.month}/{today.day}/{filename}'


class User(AbstractUser):
    class Role(models.IntegerChoices):
        ADMIN = 1, _('ادمین')
        TEACHER = 2, _('معلم')
        STUDENT = 3, _('شاگرد')
        PARENT = 4, _('والد')

    class Gender(models.IntegerChoices):
        MALE = 1, _('مرد')
        FEMALE = 2, _('زن')

    role = models.IntegerField(choices=Role.choices, verbose_name=_('نقش'), default="1")
    gender = models.IntegerField(choices=Gender.choices, blank=True, null=True, verbose_name=_('جنسیت'))
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name=_('شماره تماس'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('تاریخ ساخت'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('آخرین بروزرسانی'))
    profile_picture = models.ImageField(
        'تصویر پروفایل',
        upload_to=profile_image_upload_path,
        blank=True,
        null=True
    )


    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
