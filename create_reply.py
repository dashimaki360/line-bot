# -*- coding: utf-8 -*-

from __future__ import unicode_literals

RESPONSE_DICT = {
        '住所,場所,どこ': '海のなかだよーふーん',
        '食べ物': 'ぎょーざがだいすきなの おーしょーいきたいなあ',
        'おはよう': 'おはよーーしろたんだよ====',
        'こんにちわ,こんにちは': 'こんにちわ!!!ーーしろたんだよ====',
    }
FIX_MSG = "あたししろたんむつかしいことはよくわからないし もちもちしたものがたべたいなあ"


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

    reply = FIX_MSG
    return reply


def createReply(txt_msg):
    # reply = reverseMsg(txt_msg)
    reply = dictMsg(txt_msg)
    return reply
