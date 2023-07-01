from django.http import JsonResponse
from .models import Event
import requests,json
from django.middleware.csrf import get_token
from django.core.serializers.json import DjangoJSONEncoder

# -----------------追加分----------------------------

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

#CSFRトークン
def csrf_token(request):
    return JsonResponse({"token": get_token(request)})

#イベント新規作成
def create_event(request):
    if request.method == 'POST':
        auth_token = request.META.get("HTTP_AUTHORIZATION")
        user_id = get_github_user_id(request,auth_token.split(" ")[1])
        if user_id is None:
            return JsonResponse({'error': 'Invalid user or access token.'}, status=400)
        
        json_data = json.loads(request.body)
        event_name = json_data.get('event_name')
        timestamp = json_data.get('timestamp')
        total = json_data.get('total')
        data = json_data.get("data")
        
        event = Event.objects.create(user=user_id, event_name=event_name,timestamp=timestamp,total=total,data=data)
        return JsonResponse({'id': event.id,})
    
# イベント一覧を取得
def get_events(request):
    auth_token = request.META.get("HTTP_AUTHORIZATION")
    user_id = get_github_user_id(request,auth_token.split(" ")[1])
    if user_id is None:
        return JsonResponse({'error': 'Invalid user or access token.'}, status=400)
    
    #データベースからユーザーに関連するイベントを取得
    events = Event.objects.filter(user=user_id).values('id','event_name','timestamp', 'total')
    event_list = []
    for event in events:
        event_list.append({
            'id': event['id'],
            'event_name': event['event_name'],
            'timestamp': event['timestamp'],
            'total': event['total']
        })
    return JsonResponse(event_list, safe=False)

# イベントの詳細を取得
def get_event_detail(request, event_id):
    auth_token = request.META.get("HTTP_AUTHORIZATION")
    user_id = get_github_user_id(request,auth_token.split(" ")[1])
    if user_id is None:
        return JsonResponse({'error': 'Invalid user or access token.'}, status=400)
    
    #データベースから対応するイベントを取得
    event = Event.objects.filter(user=user_id, id=event_id).first()
    #ある場合データを返す
    if event:
        event_data = event.data
        return JsonResponse({'event_id': event_id, 'data': event_data}, encoder=DjangoJSONEncoder)
    # ない場合：エラー
    else:
        return JsonResponse({'error': 'Event not found'}, status=404)

#イベントの更新
def event_update(request, event_id):
    auth_token = request.META.get("HTTP_AUTHORIZATION")
    user_id = get_github_user_id(request,auth_token.split(' ')[1])
    if user_id is None:
        return JsonResponse({'error': 'Invalid user or access token.'}, status=400)
    
    try:
        event = Event.objects.get(id=event_id, user=user_id)
    except Event.DoesNotExist:
        return JsonResponse({'error': 'Event not found'}, status=404)
    
    if request.method == 'GET':
        # イベントデータを取得してレスポンスとして返す
        return get_event_detail(request, event_id)
    elif request.method == 'PUT':
        json_data = json.loads(request.body)
        data = json_data.get("data")
        if data:
            event.event_name = json_data.get("event_name", event.event_name)
            event.timestamp = json_data.get("timestamp", event.timestamp)
            event.total = json_data.get("total", event.total)
            event.data = data
            event.save()
            return JsonResponse({'message': 'Event updated successfully'})
        else:
            return JsonResponse({'error': 'Invalid data'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)