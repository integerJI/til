from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('kakao_login_page/', views.kakao_login_page, name='kakao_login_page'),
    path('kakao_login/', views.kakao_login, name='kakao_login'),
    path('kakao_callback/', views.kakao_callback, name='kakao_callback'),
]
