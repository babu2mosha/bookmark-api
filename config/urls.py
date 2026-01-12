from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("✅ Bookmark API is running successfully")



urlpatterns = [
    path('', home),
    
    path('admin/', admin.site.urls),

    # Bookmark APIs
    path('api/', include('bookmarks.urls')),

    # DRF login/logout
    path('api-auth/', include('rest_framework.urls')),

    # dj-rest-auth
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    # allauth (Google OAuth)
    path('accounts/', include('allauth.urls')),
]
