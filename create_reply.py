# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import random

RESPONSE_DICT = {
        '住所,場所,どこ': '海のなかだよーふーん',
        '食べ物,たべもの': 'ぎょーざがだいすきなの おーしょーいきたいなあ',
        'おはよう,おはよー,おはー': 'おはよーーしろたんだよ====',
        'こんにちわ,こんにちは': 'こんにちわ!!!ーーしろたんだよ====',
        'Hello,hello,hi,Hi': "Hello!! \"Im Shirotan\" Please call me \"TARO\"! ",
        "疲れた,つかれた,つかれたー": "げんきだして\nぼくをもふもふしていいよ",
    }
FIX_REPLY_LIST = [
    "ぼくしろたんむつかしいことはよくわからないし\nもちもちしたものがたべたいなあ",
    "ぼくしろたん",
    "ぽかぽかだねー",
    "おなかすいたなー",
    "おさんぽいこーっと",
]


def reverseMsg(msg):
    gsm = msg[::-1]
    return gsm


def dictMsg(msg):
    for dictKey in RESPONSE_DICT.keys():
        words = dictKey.split(',')
        for word in words:
            if word in msg:
                reply = RESPONSE_DICT[dictKey]
                return reply

    reply = random.choice(FIX_REPLY_LIST)
    return reply


def createReply(txt_msg):
    # reply = reverseMsg(txt_msg)
    reply = dictMsg(txt_msg)
    return reply
