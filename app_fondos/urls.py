
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('vista_previa',include('vista_previa.urls')),
    path('admin/', admin.site.urls),
]
