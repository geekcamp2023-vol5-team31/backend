# backend
技育キャンプvol5 バックエンドリポ

# API利用方法
## イベントデータの保存：
__エンドポイント:__ /myapp/save_data/

__HTTPメソッド:__ POST

__ヘッダー:__

- Authorization: Bearer {GitHubアクセストークン}
- Content-Type: application/json
  
__ボディー:__ イベントデータを表すJSONオブジェクト

__レスポンス:__  { 'success': True }
***
## イベントデータの取得：

__エンドポイント:__ /myapp/event_list/

__HTTPメソッド:__  GET

__ヘッダー:__ Authorization: Bearer {GitHubアクセストークン}

__レスポンス:__ 認証されたユーザーに関連付けられたすべてのイベントデータを含むJSON配列
***
## CSRFトークンの取得：
__エンドポイント:__ /myapp/csrf_token/

__HTTPメソッド:__  GET

__レスポンス:__ { "token": {CSRFトークン} }

# myapp/views.py
### get_github_user_id(access_token):
  
GitHub アクセストークンを使用して GitHub API からユーザーIDを取得

- 入力
  
    access_token: (string) GitHub API にリクエストを送るための認証用アクセストークン

- 出力
  
    成功時：ユーザーID（整数型）

    失敗時（HTTPステータスコードが200以外の場合）：None

### save_data(request):
ユーザーから受け取ったデータはイベントとして保存
イベントは特定のGitHubユーザーIDに関連付ける
- 入力

    request: クライアントからのHTTPリクエスト情報
    
- 出力

    成功時：JSON形式 {'success': True} となる


### event_list(request):
  
ユーザーは自身のイベントリストを取得

これらのイベントは、ユーザーIDによってフィルタリングされ
る

- 入力

    request: クライアントからのHTTPリクエスト情報

- 出力

     ユーザーに関連付けられたすべての Event オブジェクトのデータを含むJSON形式

### csrf_token(request):
  
DjangoのCSRFトークンを取得し、そのトークンをJSON形式で返す
- 入力
  

    request: クライアントからのHTTPリクエスト情報


- 出力

    key:"token"、value:"CSRFトークン"のJSON形式
