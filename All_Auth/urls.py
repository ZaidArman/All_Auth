<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView # use generic views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='dashboard/home.html'), name='home'),
    path('login', TemplateView.as_view(template_name='account/login.html'), name='login'),
    path('accounts/', include('allauth.urls')),
]
=======
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='dashboard/home.html'), name='home'),
    path('login', TemplateView.as_view(template_name='account/login.html'), name='login'),
    path('accounts/', include('allauth.urls')),
    
]
>>>>>>> eaee593af9b42438a0d4098d3e1fe016e59010e4
