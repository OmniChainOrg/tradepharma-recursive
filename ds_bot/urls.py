# ds_bot/urls.py
from django.urls import path
from ds_bot import views

app_name = 'ds_bot'  # Optional but good practice for namespaced URLs

urlpatterns = [
    path('items/', views.ItemViewSet.as_view({'get': 'list'}), name='item-list'),
    path('matches/', views.MatchList.as_view(), name='match-list'),
]
