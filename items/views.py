from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

# Create your views here.
def items(request):
    return render(request, 'items.html')

def keyboard(request):
    return JsonResponse(
        {
            # 'type':'buttons',
            # 'buttons':['내주변헌혈','공여자정보요청','수혜자정보요청']
            'type': 'text'
        }
    )

@csrf_exempt
def message(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    # json_str = ((request.body).decode('utf-8'))
    # received_json_data = json.loads(json_str)
    # cafeteria_name = received_json_data['content'].encode('utf-8')

    if return_str == '테스트':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': "테스트 성공입니다."
                    }
                }],
                'quickReplies': [{
                    'label': '처음으로',
                    'action': 'message',
                    'messageText': '처음으로'
                }]
            }
        })

# @csrf_exempt
# def message(request):

#     #button = ['내주변헌혈','공여자정보요청','수혜자정보요청']

#     json_str = (request.body).decode('utf-8')
#     received_json = json.loads(json_str)
#     content_name = received_json['content']

#     #user_name = received_json['user_key']
#     #user_name은 사용자를 구별하기 위해 사용됨
#     #type_name = received_json['type']
#     #type_name은 사용자가 보낸 값의 속성을 구별(text,photo 등)

#     if content_name == "내주변헌혈":
#         return JsonResponse(
#             {
#                 'message': {
#                     'text': '내주변헌혈을 눌렀습니다.'
#                 },
#                 'keyboard': {
#                     'type': 'buttons',
#                     'buttons': ['내주변헌혈','공여자정보요청','수혜자정보요청']
#                 }
#             }
#         )
#     elif content_name == "공여자정보요청":
#         return JsonResponse(
#             {
#                 'message': {
#                     'text': '공여자정보요청을 눌렀습니다'
#                 },
#                 'keyboard': {
#                     'type': 'buttons',
#                     'buttons': ['내주변헌혈','공여자정보요청','수혜자정보요청']
#                 }
#             }
#         )
#     elif content_name == '수혜자정보요청':
#         return JsonResponse(
#             {
#                 'message': {
#                     'text': '수혜자정보요청을 눌렀습니다'
#                 },
#                 'keyboard': {
#                     'type': 'buttons',
#                     'buttons': ['내주변헌혈','공여자정보요청','수혜자정보요청']
#                 }
#             }
#         )