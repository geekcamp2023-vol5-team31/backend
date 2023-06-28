from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Event, Participant
import requests

#保存イベント一覧：
def event_list(request):
    events = Event.objects.all()
    event_list = []
    for event in events:
        event_list.append({
            'id': event.data.get('id'),
            'date': event.data.get('date'),
            'name': event.data.get('name')
        })
    return JsonResponse(event_list, safe=False)

#イベント詳細情報
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)  
    participants = Participant.objects.filter(event=event)
    participant_list = []
    
    #データJSON形式
    for participant in participants:
        participant_data = {
            'name': participant.user.username,
            'paid_amount': str(participant.paid_amount),
            'collection_amount': str(participant.collection_amount),
            'return_amount': str(participant.return_amount)
        }
        participant_list.append(participant_data)
    event_data = {
        'event_name': event.name,
        'date': event.date.strftime('%Y/%m/%d'),
        'participants': participant_list
    }
    #JSON形式でクライアントに返す
    return JsonResponse(event_data, safe=False)

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
