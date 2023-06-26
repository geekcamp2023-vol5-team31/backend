from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.forms import SignupForm
from django.contrib.auth.models import User
# Create your views here.

# #ユーザーアカウントの登録
def signup_view(request):
    # POST
    if request.method == 'POST':
        #インスタンス作成
        form = SignupForm(request.POST)
        if form.is_valid():
            #新しいユーザーオブジェクトを保存
            form.save()
            # return HttpResponseRedirect()
            pass
    # GET
    else:
        #インスタンスを作成
        form = SignupForm()
        
    context = {'form': form}
    pass
    # return render()

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
                #成功,画面遷移
                pass
                # return HttpResponseRedirect()
            else:
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            # アカウント利用不可
            return HttpResponse("ログインIDまたはパスワードが間違っています")
        
    #GET
    else:
        pass
        # return render()

#ユーザーのログアウト    
def logout_view(request):
    pass

#ログインユーザーの情報の表示
def user_view(request):
    pass