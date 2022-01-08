from django.shortcuts import render, redirect
from project.settings import SOCIAL_OUTH_CONFIG
from .exception import KakaoException
import requests
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def index(request):
    return render(request, 'index.html')

def kakao_login_page(request):
    return render(request, 'kakao_login.html')

def kakao_login(request):
    KAKAO_REST_API_KEY = SOCIAL_OUTH_CONFIG['KAKAO_REST_API_KEY']
    KAKAO_REDIRECT_URI = SOCIAL_OUTH_CONFIG['KAKAO_REDIRECT_URI']
    
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={KAKAO_REST_API_KEY}&redirect_uri={KAKAO_REDIRECT_URI}&response_type=code"
    )

def kakao_callback(request):
    try:
    	#(1)
        code = request.GET.get("code")
        KAKAO_REST_API_KEY = SOCIAL_OUTH_CONFIG['KAKAO_REST_API_KEY']
        # client_id = os.environ.get("KAKAO_ID")
        KAKAO_REDIRECT_URI = SOCIAL_OUTH_CONFIG['KAKAO_REDIRECT_URI']
        # REDIRECT_URI = "http://127.0.0.1:8000/users/login/kakao/callback"

        #(2)
        token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={KAKAO_REST_API_KEY}&redirect_uri={KAKAO_REDIRECT_URI}&code={code}"
        )
        
        #(3)
        token_json = token_request.json()
        error = token_json.get("error", None)
        if error is not None:
            raise KakaoException()
        #(4)
        access_token = token_json.get("access_token")
        #(5)
        profile_request = requests.get("https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"},)
        profile_json = profile_request.json()
        #(6)
        email = profile_json.get("kakao_account", None).get("email")
        if email is None:
            raise KakaoException()
        properties = profile_json.get("properties")
        nickname = properties.get("nickname")
        profile_image = properties.get("profile_image")
        #(7)
        try:
            user = User.objects.get(email=email)
            if user.login_method != User.LOGIN_KAKAO:
                raise KakaoException()
        except User.DoesNotExist:
            user = User.objects.create(
                username=email,
                email=email,
                email_verified=True,
            )
            user.set_unusable_password()
            user.save()
            #(8)
        auth.login(request, user)
        return redirect("/")
    except KakaoException:
        return redirect("/")



# @api_view(['GET'])
# @permission_classes([AllowAny, ])
# def kakaoGetLogin(request):
#     CLIENT_ID = SOCIAL_OUTH_CONFIG['KAKAO_REST_API_KEY']
#     REDIRET_URL = SOCIAL_OUTH_CONFIG['KAKAO_REDIRECT_URI']
#     url = "https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={0}&redirect_uri={1}".format(
#         CLIENT_ID, REDIRET_URL)
#     res = redirect(url)
#     return res

# @api_view(['GET'])
# @permission_classes([AllowAny, ])
# def getUserInfo(reqeust):
#     CODE = reqeust.query_params['code']
#     url = "https://kauth.kakao.com/oauth/token"
#     res = {
#             'grant_type': 'authorization_code',
#             'client_id': SOCIAL_OUTH_CONFIG['KAKAO_REST_API_KEY'],
#             'redirect_url': SOCIAL_OUTH_CONFIG['KAKAO_REDIRECT_URI'],
#             'client_secret': SOCIAL_OUTH_CONFIG['KAKAO_SECRET_KEY'],
#             'code': CODE
#         }
#     headers = {
#         'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
#     }
#     response = requests.post(url, data=res, headers=headers)
#     # 그 이후 부분
#     tokenJson = response.json()
#     userUrl = "https://kapi.kakao.com/v2/user/me" # 유저 정보 조회하는 uri
#     auth = "Bearer "+tokenJson['access_token'] ## 'Bearer '여기에서 띄어쓰기 필수!!
#     HEADER = {
#         "Authorization": auth,
#         "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
#     }
#     res = requests.get(userUrl, headers=HEADER)
#     return Response(res.text)
