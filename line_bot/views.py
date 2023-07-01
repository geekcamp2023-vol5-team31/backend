from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from linebot import WebhookHandler, LineBotApi
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage
import requests

CHANNEL_SECRET = 'd4307b8e64fd86590d3e92bb952e0eaa'
CHANNEL_ACCESS_TOKEN = '9U5QyS3exnmcxKYVZf5UvJ62Z6sSA6ZJxNFb6EOWtP7KAXGz4cqHdlqMxswrETYP6ddii8lZNoFpiA7stVdDC2LoswquJnSc5c2r7IR7JJUuLVYgZ42TkPEzlt6eZ7PsTH2ph3tb27doL7iU1z5HVwdB04t89/1O/w1cDnyilFU='

handler = WebhookHandler(channel_secret=CHANNEL_SECRET)
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

@csrf_exempt
def callback(request):
    """最初にこのメソッドが動く"""
    if request.method == 'POST':
        # 署名検証のための署名情報。シークレットキーと突合し、正常性を確認する。
        signature = request.headers['X-Line-Signature']
        body = request.body.decode('utf-8')

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            print("Invalid signature. Please check your channel access token/channel secret.")
            return HttpResponseForbidden()
        return HttpResponse(status=200)

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    """リプライ用 テキストが届いたら動く処理"""
    sum = 0
    if event.message.text == "わりかんじ":
        response = requests.get("https://api.line.me/v2/bot/group/{groupId}/members/count")