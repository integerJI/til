from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('kakao_login_page/', views.kakao_login_page, name='kakao_login_page'),
    path('kakao_login/', views.kakao_login, name='kakao_login'),
    path('kakao_local/', views.kakao_local, name='kakao_local'),
    path('kakao_callback/', views.kakao_callback, name='kakao_callback'),
    path('qrcode/', views.qrcode, name='qrcode'),
]
