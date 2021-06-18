from django.urls import path
from .views import ShortenerListAPIView, ShortenerCreateAPIView

urlpatterns = [
    path('', ShortenerListAPIView.as_view(), name='all_links'),
    path('create-link/', ShortenerCreateAPIView.as_view(), name='create_link'),
]