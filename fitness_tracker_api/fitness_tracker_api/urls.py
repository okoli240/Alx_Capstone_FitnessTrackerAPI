from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

def home(request):
    return HttpResponse("Welcome to the Fitness Tracker API 🚀")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    # Activities endpoints
    path('api/', include('activities.urls')),
    path('api/v1/', include('activities.urls')),

    # JWT authentication endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
