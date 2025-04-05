from django.urls import path
from .views import dashboard, redirect_url

urlpatterns = [
    path("URL.html", dashboard, name="dashboard"),  # Dashboard page
    path("<str:short_code>/", redirect_url, name="redirect_url"),  # Redirect short URLs
    
]
