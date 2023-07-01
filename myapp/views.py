from django.http import JsonResponse
from .models import Event
import requests,json
from django.middleware.csrf import get_token
from django.core import serializers

#githubユーザ認証
def get_github_user_id(request,access_token):
    if 'user_id' in request.session:
        return request.session['user_id']
    else:
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        response = requests.get('https://api.github.com/user', headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            user_id = user_data['id']
            request.session['user_id'] = user_id #セッションにuser_idを保存
            return user_id  #user_idを返す
        else:
            return None

def csrf_token(request):
    return JsonResponse({"token": get_token(request)})

# イベント一覧を取得
def get_events(request):
    auth_token = request.META.get("HTTP_AUTHORIZATION")
    user_id = get_github_user_id(auth_token.split(" ")[1])
    
    #データベースからユーザーに関連するイベントを取得
    events = Event.objects.filter(user=user_id).values('id', 'data')
    event_list = []
    for event in events:
        event_list.append({
            'id': event['id'],
            'data': event['data']
        })
    return JsonResponse(event_list, safe=False)

# イベントの詳細を取得
def get_event_detail(request, event_id):
    auth_token = request.META.get("HTTP_AUTHORIZATION")
    user_id = get_github_user_id(auth_token.split(" ")[1])
    
    #データベースから対応するイベントを取得
    event = Event.objects.filter(user=user_id, id=event_id).first()
    #ある場合データを返す
    if event:
        return JsonResponse(event.data)
    #ない場合：エラー
    else:
        return JsonResponse({'error': 'Event not found'}, status=404)

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