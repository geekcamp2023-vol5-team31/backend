# backend
技育キャンプvol5 バックエンドリポ

# json形式

    {
        'event_name':"イベント名",
        'timestamp': '2023-07-01T00:00:00',
        'data': [
            {
                'name': '参加者名1',
                'amount': 金額1,
            },
            {
                'name': '参加者名2',
                'amount': 金額2,
            },
            .
            .
            .
        ]
    }
# API利用方法

##
イベント新規作成: POST /myapp/create_event/

イベント一覧を取得: GET /myapp/get_events/

イベントの詳細を取得: GET /myapp/get_event_detail/<int:event_id>/

イベントの更新: PUT /myapp/event_update/<int:event_id>/

---
## イベント新規作成：
__エンドポイント:__ /myapp/create_event/

__HTTPメソッド:__ POST

__ヘッダー:__　Authorization: Bearer [アクセストークン]
  
__ボディー:__ JSONデータ（イベント名,作成日,参加者名，金額）

__レスポンス:__

    status=200
    {
        "event_id": [イベントID],
    }

__エラーレスポンス:__

    status=400
    {
        "error": "Invalid user or access token."
    }

***
## イベント一覧取得：

__エンドポイント:__ /myapp/get_events/

__HTTPメソッド:__  GET

__ヘッダー:__ Authorization: Bearer [アクセストークン]

__レスポンス:__ 

    status=200
    [
        {'id': 1, 'event_name': 'イベント名1', 'timestamp': '2023-07-01T00:00:00'},
        {'id': 2, 'event_name': 'イベント名2', 'timestamp': '2023-08-01T00:00:00'}, 
        ...
    ]

__エラーレスポンス:__

    status=400
    {
        "error": "Invalid user or access token."
    }

***
## イベント詳細取得：
__エンドポイント:__ /myapp/get_event_detail/<int:event_id>/

__HTTPメソッド:__  GET

__ヘッダー:__ Authorization: Bearer [アクセストークン]

__レスポンス:__ 

    status=200
    {
        'event_id': 49, 
        'event_name':"イベント名",
        'timestamp': '2023-07-01T00:00:00',
        'data': [
            {
                'name': 'UpdatedParticipant1',
                'amount': 10
            }, 
            {
                'name': 'UpdatedParticipant2', 
                'amount': 20
            }
            .
            .
            .
        ]
    }

__エラーレスポンス：__

    status=400
    {
        "error": "Invalid user or access token."
    }
    status=404
    {
        'error': 'Event not found' 
    }

---
## イベント更新：
__エンドポイント:__ /myapp/event_update/<int:event_id>/

__HTTPメソッド:__  PUT

__ヘッダー:__ Authorization: Bearer [アクセストークン]


__レスポンス:__

    status=200
    {
        "message": "Event updated successfully"
    }

__エラーレスポンス:__

    status=400
    {
        'error': 'Invalid data'
    }
    status=400
    {
        'error': 'Invalid request method'
    }
    status=400
    {
        "error": "Invalid user or access token."
    }
    status=404
    {
        'error': 'Event not found'
    }
    
