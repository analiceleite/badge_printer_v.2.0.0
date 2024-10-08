from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("authentication.urls")),
    path('home/', include("home.urls")),
    path('import/', include("import.urls")),
    path('print/', include("print.urls")),
    path('register/', include("register.urls")),
    path('support/', include("support.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

