from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Event
import requests,json
# from django.views.decorators.csrf import csrf_protect,csrf_exempt


#githubユーザ認証
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

#データ保存用
def save_data(request):
    if request.method == 'POST':
        auth_token = request.META.get("HTTP_AUTHORIZATION")
        user_id = get_github_user_id(auth_token.split(" ")[1])

        if not user_id:
            json_data = request.POST.get('data')
            data = json.loads(json_data)
            Event.objects.create(user=user_id, data=data)
            return JsonResponse({'success': True})

        else:
            json_data = request.POST.get('data')
            data = json.loads(json_data)
            Event.objects.create(user=user_id, data=data)
            return JsonResponse({'success': True})

    # POSTメソッド以外の場合はHTTP 405 Method Not Allowedを返す
    return HttpResponseNotAllowed(['POST'])
    
#保存イベント一覧：
def event_list(request, user_id):
    # ユーザ認証
    auth_token = request.META.get("HTTP_AUTHORIZATION")
    user_id = get_github_user_id(auth_token.split(' ')[1])
    
    # events = Event.objects.all()#Event取り出す
    # event_list = []
    # for event in events:#user_idと一致するか
    #     if event.user == user_id:
    #         event_list.append(event.data)
    
    events = Event.objects.filter(user=user_id)  # ユーザIDに紐づくイベントを取得
    event_list = [event.data for event in events]
            
    return JsonResponse(event_list, safe=False)#イベントリストを返す

