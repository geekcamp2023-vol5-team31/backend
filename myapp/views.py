from django.http import JsonResponse
from django.views import View
from .models import Event,Participant

#イベント情報表示画面
class EventDetailsView(View):
    #GET
    def get(self, request, *args, **kwargs):
        
        #イベントIDを取得
        event_id = self.kwargs.get('event_id')
        
        #イベントをデータベースから探す
        event = Event.objects.filter(id=event_id).first()
        
        #イベントがない：エラー出力
        if event is None:
            return JsonResponse({'エラー': '指定されたイベントは存在しません。'})
        
        #参加者をデータベースから取得
        participants = Participant.objects.filter(event=event)
        
        #データ作成JSON形式
        data = {
            'イベント名': event.name,
            '日付': event.date.isoformat(),
            '支払総額': str(event.total_amount),
            '徴収額': str(event.total_amount / participants.count()),
            '参加者': [{
                'ユーザー名': participant.user.username,
                '預かった金額': str(participant.paid_amount),
                '返す金額': str(participant.paid_amount - (event.total_amount / participants.count())),
            } for participant in participants]
        }
        
        #JSON形式でクライアントに返す
        return JsonResponse(data, safe=False)
