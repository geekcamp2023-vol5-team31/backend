from django.http import JsonResponse
from .models import Event
import requests,json
from django.middleware.csrf import get_token

#githubユーザ認証
# @csrf_exempt
def get_github_user_id(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get('https://api.github.com/user', headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data['id']
        return user_id  #user_idを返す
    else:
        return None

def CsrfToken(request):
    return JsonResponse({"token": get_token(request)})

#データ保存用
def save_data(request):
    #POST
    if request.method == 'POST':
        # ユーザ認証
        auth_token = request.META.get("HTTP_AUTHORIZATION")
        user_id = get_github_user_id(auth_token.split(" ")[1])
        tmp = Event.objects.filter(user=user_id)
        if len(tmp) == 0: 
            data = json.loads(request.body)
            Event.objects.create(user=user_id, data=data)
            return JsonResponse({'success': True})
        else:
            data = json.loads(request.body)         #json解析
            Event.objects.create(data=data)      #データベースに保存
            return JsonResponse({'success': True})  #成功レンスポンス
    
#保存イベント一覧：
def event_list(request):
    # ユーザ認証
    auth_token = request.META.get("HTTP_AUTHORIZATION")
    access_token = auth_token.split(' ')[1]
    user_id = get_github_user_id(access_token)
    event_lists = Event.objects.filter(user=user_id).all()
    event_list = []
    for event in event_lists:
        event_list.append(json.dumps(event.data))
    return JsonResponse(event_list, safe=False)#イベントリストを返す