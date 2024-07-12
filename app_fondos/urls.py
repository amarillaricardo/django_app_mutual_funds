from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('datos_generales',include('datos_generales.urls')),
    path('cuotapartes/',include('cuotapartes.urls')),
    path('usuarios',include('usuarios.urls')),
    path('accounts/', include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, documen_root=settings.MEDIA_ROOT)


