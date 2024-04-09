from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView # use generic views
# from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='dashboard/home.html'), name='home'),
    path('login', TemplateView.as_view(template_name='account/login.html'), name='login'),
    path('accounts/', include('allauth.urls')),
    
    # path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    
    # path('dj-rest-auth/twitter/connect/', TwitterConnect.as_view(), name='twitter_connect'),
    
    # path('dj-rest-auth/apple/connect/', AppleConnect.as_view(), name='apple_connect'),
]