from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Event, Participant
import requests,json

#データ保存用
def save_data(request,user_id):
    #POST
    if request.method == 'POST':
        # ユーザ認証
        user_id = get_github_user_id(user_id)
        if not user_id:
            return JsonResponse({'error': 'ユーザが認証失敗'}, status=401)
        
        json_data = request.POST.get('data') #フロントから渡されるデータ
        data = json.loads(json_data)         #json解析
        Event.objects.create(data=data)      #データベースに保存
        return JsonResponse({'success': True})  #成功レンスポンス
    
#保存イベント一覧：
def event_list(request, user_id):
    auth_token = get_github_user_id(request.META.get("HTTP_AUTHORIZATION"))
    access_token = auth_token.split(' ')[1]
    user_id = get_github_user_id(access_token)
    events = Event.objects.all()
    event_list = []
    for event in events:
        if event.user == user_id:
            event_list.append(event.data)
    return JsonResponse(event_list, safe=False)

#github api
def get_github_user_id(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get('https://api.github.com/user', headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data['id']
        return user_id
    else:
        return None
