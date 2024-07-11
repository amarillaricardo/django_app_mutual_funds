
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('cuotapartes',include('cuotapartes.urls')),
    path('usuarios',include('usuarios.urls')),
    path('vista_previa',include('vista_previa.urls')),
    path('accounts/', include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
]
