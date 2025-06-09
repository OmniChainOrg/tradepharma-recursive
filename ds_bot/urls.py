
# ds_app/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ds_bot.api import ItemViewSet  # your DRF viewset

app_name = 'ds_bot' 

# 1) Set up DRF router for the API
router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')

urlpatterns = [
    # 2) Admin
    path('admin/', admin.site.urls),

    # 3) API endpoints
    #    GET  /api/items/       → list/create
    #    GET  /api/items/{pk}/  → retrieve/update/destroy
    path('api/', include(router.urls)),

    # 4) Your existing template-based views
    #    GET  /             → views.dashboard
    #    GET  /items/       → views.item_list
    #    GET  /items/<pk>/  → views.item_detail
    path('', include('ds_bot.urls')),
]
