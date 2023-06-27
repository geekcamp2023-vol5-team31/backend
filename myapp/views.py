from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404
from .models import Event, Participant

#保存イベント一覧：
def event_list(request):
    events = Event.objects.all()
    event_list = []
    for event in events:
        event_list.append({
            'id': event.id,
            'date': event.date.strftime('%Y/%m/%d'),
            'name': event.name
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