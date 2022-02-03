from email import contentmanager
from django.shortcuts import render, redirect
from project.settings import SOCIAL_OUTH_CONFIG
from .exception import KakaoException
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import JsonResponse
from django.views import View
import requests, json
from urllib import parse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def kakao_login_page(request):
    return render(request, 'kakao_login.html')

def kakao_local(request):
    context = {
        "kakaoJsKey" : SOCIAL_OUTH_CONFIG['KAKAO_JS_KEY']
    }
    return render(request, 'kakao_local.html', context)

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

        print(profile_json)
        #(6)
        email = profile_json.get("kakao_account", None).get("email")
        if email is None:
            email = 'admin@admin.com'

        #(7)
        try:
            user = User.objects.filter(email=email)
            if user.login_method != User.LOGIN_KAKAO:
                raise KakaoException()
        except User.DoesNotExist:
            user = User.objects.create(
                username=email,
                email=email,
                login_method = "LOGIN_KAKAO",
                email_verified=True,
            )
            user.set_unusable_password()
            user.save()
            #(8)
        auth.login(request, user)
        return redirect("/")
    except KakaoException:
        return redirect("/")

def qrcode(request):
    return render(request, 'qrcode.html')

class jsonView(View):
    def get(self, request):
        return render(request, 'json.html')

    def post(self, request):
        response = {}
        
        body = request.body.decode('utf8')
        data = json.loads(body)

        response["result"] = "true"
        response["status_code"] = "200"
        response["message"] = data['title']+" 통신 성공 !!"
        response["return_url"] = "/"

        json_data = json.dumps(data)

        return JsonResponse(response, json_dumps_params = {'ensure_ascii': False})
        
def kakao_maps(request):
    context = {
        "kakaoJsKey" : SOCIAL_OUTH_CONFIG['KAKAO_JS_KEY']
    }
    return render(request, 'kakao_maps.html', context)

class urlChangeView(View):
    def get(self, request):
        return render(request, 'url_change.html')

    def post(self, request):
        response = {}
        body = request.body.decode('utf8')
        data = json.loads(body)

        encoding = data['encoding']
        url = parse.urlparse(encoding) 
        print(type(encoding))
        print(parse.parse_qs(url.query))

        data['encoding'] = encoding

        response["encoding"] = data['encoding']

        json_data = json.dumps(data)

        return JsonResponse(response, json_dumps_params = {'ensure_ascii': False})
