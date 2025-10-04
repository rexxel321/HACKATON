from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('chatbot_app.urls')),  # Correctly includes chatbot_app URLs
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])