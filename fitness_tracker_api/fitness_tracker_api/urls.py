from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Fitness Tracker API 🚀")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), 
    path('api/', include('activities.urls')),
    path('api/v1/', include('activities.urls')), 
]
