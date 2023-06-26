from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from .models import Payment

#イベント作成
def add_participant(request):
        if request.method == 'POST':
            
            name = request.POST['name']
            amount = request.POST['date']
            
            if not name or not amount:
                return JsonResponse({'error': '名前と金額は必須項目です。'},status = 400)
            
            payment = Payment(name=name, amount=amount)
            payment.save()
            
            return JsonResponse({'message': '支払い金額が正常に作成されました。', 'イベントID': event.id})
        
        else:
            return JsonResponse({'message': 'このエンドポイントはPOSTリクエストのみサポートしています'}, status=405)
            
def calculate_return(request, event_id):
    event = Event.objects.get(id=event_id)
    participants = event.participants.all()

    per_person = event.total_amount / len(participants)

    return_amounts = {}

    for participant in participants:
        return_amount = participant.paid_amount - per_person
        return_amounts[participant.user.username] = str(return_amount)

    return JsonResponse(return_amounts)

#ユーザーアカウントの登録
def signup_view(request):
    # POST
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #新しいユーザーオブジェクトを保存
            form.save()
            #成功
            return JsonResponse({'message': 'ユーザー登録が成功しました。'})
        else:
            #失敗
            return JsonResponse({'errors': form.errors}, status=400)
    # GET
    else:
        form = UserCreationForm()
        
    context = {'form': form}
    return JsonResponse(context)

#ユーザーのログイン
def login_view(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Djangoの認証機能
        user = authenticate(request, username=username, password=password)

        #ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                #ログイン
                login(request, user)
                #成功
                return JsonResponse({'message': 'ログイン成功しました'})
            else:
                return JsonResponse({'error': 'アカウントが有効ではありません'}, status=400)
        # ユーザー認証失敗
        else:
            # アカウント利用不可
            return JsonResponse({'error': '無効なユーザー名またはパスワードです'}, status=400)
        
    #GET
    else:
        return JsonResponse({'message': 'このエンドポイントはPOSTリクエストのみサポートしています'}, status=405)

#ユーザーのログアウト    
def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'ログアウトしました'})

#ログインユーザーの情報の表示
@login_required
def user_view(request):
    user = request.user
    return JsonResponse({'username': user.username})