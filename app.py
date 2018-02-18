# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys
import random
from datetime import datetime
import json

import create_reply

from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    StickerMessage, StickerSendMessage,
)


app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', None)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class usermessage(db.Model):
    __tablename__ = 'usermessage'
    id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.String(50))
    message = db.Column(db.Text)
    birth_date = db.Column(db.TIMESTAMP)

    def __init__(self,
                 id,
                 user_id,
                 message,
                 timestamp,):
        self.id = id
        self.user_id = user_id
        self.message = message
        self.timestamp = timestamp

    def to_dict(self):
        return dict(
            id=self.id,
            user_id=self.user_id,
            message=self.message,
            timestamp=self.timestamp,
        )


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    bodyjson = json.loads(body)
    app.logger.info("Request body: " + body)

    # add message data to sql
    add_data = usermessage(
            id=bodyjson['events'][0]['message']['id'],
            user_id=bodyjson['events'][0]['source']['userId'],
            message=bodyjson['events'][0]['message']['text'],
            timestamp=datetime.fromtimestamp(int(bodyjson['events'][0]['timestamp'])/1000)
        )
    db.session.add(add_data)
    db.session.commit()

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    msg = event.message.text
    reply = create_reply.createReply(msg)

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply)
    )


@handler.add(MessageEvent, message=StickerMessage)
def message_sticker(event):
    sticer_id = random.randint(180, 307)
    if sticer_id < 260:
        package_id = 3
    else:
        package_id = 4

    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(
            package_id=package_id,
            sticker_id=sticer_id,
        )
    )


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
