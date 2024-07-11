
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('datos_generales',include('datos_generales.urls')),
    path('cuotapartes/',include('cuotapartes.urls')),
    path('usuarios',include('usuarios.urls')),
    path('accounts/', include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
]
