from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from accounts.views import register_view, home_view


urlpatterns = [
    path('', home_view, name='home'),  # مسیر خالی (خانه)
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
