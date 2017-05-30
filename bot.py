$ pip install line-bot-sdk
rom flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('qgdntcUqQibpcFZwTLOarjqCmPtXS/d5E8zovhoZS/Rd7e1Ue0JLVMzSGLwQB6r4+rDpddQcEBRILXlWXA4X80ZNWRToRf1ex1oi2RqR/jXjb/iNQbHjlZmxnqLfgKDnnlSa1KWeGtWqxptHoD0dGgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7965194bb5461e9e05a7789d0deae092')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
    
 return 'OK'
