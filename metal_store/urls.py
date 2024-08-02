from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls', namespace='store')),
    path('', include('contacts.urls', namespace='contacts'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, )
