# coding: utf-8
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (    MessageEvent, TextMessage, TextSendMessage,SourceUser, SourceGroup, SourceRoom,TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,ButtonsTemplate, URITemplateAction, PostbackTemplateAction,CarouselTemplate, CarouselColumn, PostbackEvent,StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,ImageMessage, VideoMessage, AudioMessage,UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent)
import base64
import hashlib
import hmac
import json
import requests
import os
import sys
import telebot



app = Flask(__name__)

bot = telebot.TeleBot("Telegram-Bot-API")
chatid = "Telegram-channlName"
line_bot_api = LineBotApi('LINE-Channel-Access-Token')
handler = WebhookHandler('LINE-Channel-Secret')


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
def handle_text_message(event):
    rep = event.reply_token
    text = event.message.text

    bot.send_message(chatid, text)




if __name__ == "__main__":
    app.run(port=os.environ['PORT'], host='0.0.0.0')
