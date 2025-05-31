from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .decorators import user_is_self_or_admin
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView


def home_view(request):
    """
    صفحه اصلی پروژه مکتب.
    نمایش نوار ناوبری با دکمه‌های ورود، ثبت‌نام و خروج بر اساس وضعیت کاربر.
    """
    return render(request, 'accounts/home.html')



class MyLoginView(LoginView):
    template_name = 'accounts/login.html'

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'ثبت‌نام با موفقیت انجام شد! اکنون می‌توانید وارد شوید.')
            return redirect('login')  # یا هر URL دلخواه برای ورود
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
@user_is_self_or_admin
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})