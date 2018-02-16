# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import random

RESPONSE_DICT = {
        '住所': '海のなかだよーふーん',
        '場所': '海のなかだよーふーん',
        'どこ': '海のなかだよーふーん',
        '食べ物': 'ぎょーざがだいすきなの おーしょーいきたいなあ',
        'たべもの': 'ぎょーざがだいすきなの おーしょーいきたいなあ',
        'おはよう': 'おはよーーしろたんだよ====',
        'おはよー': 'おはよーーしろたんだよ====',
        'おはー': 'おはよーーしろたんだよ====',
        'こんにちわ': 'こんにちわ!!!ーーしろたんだよ====',
        'こんにちは': 'こんにちわ!!!ーーしろたんだよ====',
        'hello': "Hello!! \"Im Shirotan\" Please call me \"TARO\"! ",
        'hi': "Hello!! \"Im Shirotan\" Please call me \"TARO\"! ",
        "疲れた": "げんきだして\nぼくをもふもふしていいよ",
        "つかれた": "げんきだして\nぼくをもふもふしていいよ",
        "つかれたー": "げんきだして\nぼくをもふもふしていいよ",
    }
FIX_REPLY_LIST = [
    "ぼくしろたんむつかしいことはよくわからないし\nもちもちしたものがたべたいなあ",
    "ぼくしろたん",
    "ぽかぽかだねー",
    "おなかすいたなー",
    "おさんぽいこーっと",
]

'''
def reverseMsg(msg):
    gsm = msg[::-1]
    return gsm
'''


def dictMsg(msg):
    for dictKey in RESPONSE_DICT.keys():
        if dictKey.lower() in msg.lower():
            reply = RESPONSE_DICT[dictKey]
            return reply

    reply = random.choice(FIX_REPLY_LIST)
    return reply


def createReply(txt_msg):
    reply = dictMsg(txt_msg)
    return reply
