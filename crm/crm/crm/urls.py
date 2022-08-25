from django.conf.urls import include
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from crm import settings

urlpatterns = [
    path('', include('work.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls)
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
