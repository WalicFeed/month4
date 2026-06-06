from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('', include('race.urls')),
    path('', include('myShop.urls')),
    path('', include('BASKET.urls')),
    path('', include('ankets2.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)