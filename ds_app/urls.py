# ds_app/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('ds_bot.urls')),  # Includes URLs from ds_bot/urls.py
]
