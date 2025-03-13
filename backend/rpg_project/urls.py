from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/adventures/', include('adventures.urls')),
    path('api/chat/', include('chat.urls')),
    path('api/game/', include('game.urls')),
    ] 

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),  # Add Debug Toolbar URL
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)