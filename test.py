# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import create_reply as cre

if __name__ == "__main__":
    # create reply test
    print(cre.dictMsg("住所"))
    print(cre.dictMsg("場所"))
    print(cre.dictMsg("どこ"))
    print(cre.dictMsg("食べ物"))
    print(cre.dictMsg("おはよう"))
    print(cre.dictMsg("こんにちわ"))
    print(cre.dictMsg("こんにちは"))
    print(cre.dictMsg("hoge"))

    print(cre.dictMsg("どこ住所"))
    print(cre.dictMsg("食べ物住所"))
    print(cre.dictMsg("fdjakl;fnmeoipafeoaef"))
    print(cre.dictMsg("hofewsanle住所ほがだれj"))