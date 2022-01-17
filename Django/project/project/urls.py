from django.contrib import admin
from django.urls import path, include
from qr_code import urls as qr_code_urls
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('app/', include('app.urls')),
    path('qr_code/', include(qr_code_urls, namespace='qr_code')),
]
