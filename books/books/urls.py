
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('books/', include('book.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls'))
]
