from django.shortcuts import render, get_object_or_404, redirect
import urllib
from django.views import View
import allauth

# Create your views here.



















class KakaoLoginVIew(View):
    def get(self, request):
        kakao_access_code = request.GET.get('code', None)

        url = 'https://kauth.kakao.com/oauth/token'

        headers = {'Content_type': 'application/x-www-form-urlencoded; charset=utf-8'}

        body = {'grant_type' : 'authorization_code',
                'client_id' : 'beb7c6a8d954a47c48242ba1c1dac2d4',
                'redirect_uri' : 'http://127.0.0.1:8000/account/login/kakao/callback',
                'code': kakao_access_code
                }
        token_kakao_response = request.post(url, headers = headers, data = body)

        access_token = json.loads(token_kakao_response.text).get('access_token')

        url = 'https://kapi.kako.com/v2/user/me'
        headers = {
            'Authorization' : f'Bearer {access_token}',
            'Content-type': 'applicationapplication/x-www-form-urlencoded; charset=utf-8'
        }

        kakao_response = requests.get(url, headers = headers)
        kakao_response = json.loads(kakao_response.text)
        kakao = Socialplatform.objects.get(platform.text)
        return HttpResponse(f'{kakao_response.text}')







# def oauth(request):
#     code = request.GET['code']
#     print('code= ' + str(code))

#     client_id = 'beb7c6a8d954a47c48242ba1c1dac2d4'
#     redirect_uri = 'http://127.0.0.1:8000/account/login/kakao/callback'
#     access_token_request_uri = "https://kauth.kakao.com/oauth/token?grant_type=authorization_code&"

#     access_token_request_uri += "client_id=" + client_id
#     access_token_request_uri += "&redirect_uri=" + redirect_uri
#     access_token_request_uri += "&code=" + code
#     print(access_token_request_uri)

#     access_token_request_uri_data = requests.get(access_token_request_uri)
#     json_data = access_token_request_uri_data.json()
#     access_token = json_data['access_token']
#     print(access_token)

#     user_profile_info_uri = "https://kapi.kakao.com/v2/user/me?access_token="
#     user_profile_info_uri += str(access_token)
#     print(user_profile_info_uri)

#     user_profile_info_uri_data = requests.get(user_profile_info_uri)
#     user_json_data = user_profile_info_uri_data.json()
#     user_nickname = user_json_data['properties']['nickname']
#     print(user_nickname)

#     return redirect('index')

# def kakao_login(request):
#     login_request_uri = 'https://kauth.kakao.com/oauth/authorize?'
#     client_id = 'beb7c6a8d954a47c48242ba1c1dac2d4'
#     redirect_uri = 'http://127.0.0.1:8000/account/login/kakao/callback'

#     login_request_uri += 'client_id=' + client_id
#     login_request_uri += '&redirect_uri=' + redirect_uri
#     login_request_uri += '&response_type=code'

#     return redirect(login_request_uri)

# #코드요청
# def kakao_login(request):
#     app_rest_api_key = 'beb7c6a8d954a47c48242ba1c1dac2d4'
#     redirect_uri = "http://127.0.0.1:8000/account/login/kakao/callback"
#     return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={redirect_uri}&responsee_type=code")

# #access token 요청
# def kakao_callback(request):
#     params = urllib.parse.urlencode(request.GET)
#     return redirect(f'http://127.0.0.1:8000/account/login/kakao/callback?{params}')