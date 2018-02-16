# -*- coding: utf-8 -*-

from __future__ import unicode_literals


def reverseMsg(msg):
    gsm = msg[::-1]
    return gsm


def createReply(txt_msg):
    reply = reverseMsg(txt_msg)
    return reply
