import random, redis, os, locale
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core.cache import cache
from django.conf import settings


def apipk(request, userid):
    """
    HOP
    """
    # print(userid)
    pk_user = ["东", "北", "西", "南"]
    pk_num = cache.get('pk_num')
    print(request.POST)
    # print("init:",type(request.POST.get("init")))
    # print("suit:",type(request.POST.get("suit")))
    # print("card:",type(request.POST.get("card")))
    # print("sync:",type(request.POST.get("sync")))

    pk_dict = {}

# 出牌
    if(request.POST.get("suit")=="1"):
        suitcard = request.POST.get("card").split(",")
        suitnum = request.POST.get("num").split(",")
        suitnum.reverse()
        # print(suitnum)        
        # print(suitnum)
        pk_card = cache.get('pk_card')
        pk_cur = cache.get('pk_cur')
        pk_cur_cache = []
        count = 0
        for s in suitnum:
            pk_card[userid].pop(int(s))
            pk_cur_cache.append(int(suitcard[count]))
            count = count + 1

        pk_cur.append(pk_cur_cache)
        pk_hold = userid + 1
        if (pk_hold> (pk_num-1)):
            pk_hold = 0
        cache.set('pk_cur', pk_cur, settings.REDIS_TIMEOUT)
        cache.set('pk_card', pk_card, settings.REDIS_TIMEOUT)
        cache.set('pk_hold', pk_hold, settings.REDIS_TIMEOUT)

        # print(pk_cur)
        # print(pk_card)
        # print(cache.get('p0'))
        pk_dict = {
            'msg':"已出牌",
            }
# 撤销出牌        
    if(request.POST.get("suit")=="2"):
        pk_cur = cache.get('pk_cur')
        pk_cur_len = len(pk_cur)
        pk_card = cache.get('pk_card')
        suitcard = []
        # print(pk_cur_len)
        # print(pk_cur)
        pk_dict = {
            'msg':"无牌可取",
            }   
        if (pk_cur_len):            
            suitcard = pk_cur.pop()   
            pk_card[userid] = pk_card[userid] + suitcard
            pk_card[userid].sort()
            # print(pk_card)
            cache.set('pk_card', pk_card, settings.REDIS_TIMEOUT)
            cache.set('pk_cur', pk_cur, settings.REDIS_TIMEOUT)
            pk_dict = {
                'msg':"已取回",
                }      

#  勾叉以及设置当前出牌者
    if(request.POST.get("suit")=="3"):
        cache.set('pk_hold', userid, settings.REDIS_TIMEOUT)
        pk_dict = {
            'msg':"设置当前玩家为出牌者",
            }
#  出牌者放弃出牌

    if(request.POST.get("suit")=="4"):
        pk_hold = userid + 1
        if (pk_hold> (pk_num-1)):
            pk_hold = 0
        cache.set('pk_hold', pk_hold, settings.REDIS_TIMEOUT)
        pk_dict = {
            'msg':"放弃出牌",
            }


# 定时同步数据
    if(request.POST.get("sync")=="1"):
        pk_card = cache.get('pk_card')
        pk_cur = cache.get('pk_cur')
        pk_hold = cache.get('pk_hold')
        if (len(pk_card)):
            # print(pk_card)
            pass
        else:
            pk_card = []     

        if (len(pk_cur)):
            suitcard = pk_cur[-1]
        else:
            suitcard = []

        pk_dict = {
            'cards': pk_card,
            'cur': suitcard,
            'hold': pk_hold,
            }
    pk_msg = "初始化界面，同步用户名称\n 当前局人数：{0}。".format(pk_num)
#  提供UI初始化组件， 获取用户ID
    if(request.POST.get("init")=="99"):
        pk_dict = {
            'players': pk_user,
            'userid': userid,
            'holdid': userid,
            'msg':pk_msg,
            }

# 初始化4人牌局
    if(request.POST.get("init")=="4"):
        pk_num = int(request.POST.get("pnum"))
        cache.set('pk_num', pk_num, settings.REDIS_TIMEOUT)

        pk_all = list(range(54))
        # print(pk_all)
        random.shuffle(pk_all)
        # print(pk_all)
        if (pk_num == 4):
            pk_user = ["东", "北", "西", "南"]

            p0 = pk_all[:14]
            p0.sort()
            p1 = pk_all[14:28]
            p1.sort()
            p2 = pk_all[28:41]
            p2.sort()
            p3 = pk_all[41:54]
            p3.sort()
            pk_card = [p0,p1,p2,p3]
            pk_cur = []
            pk_dict = {
                'players': pk_user,
                'userid': userid,
                'holdid': 0,
                'msg':pk_msg
                }
            cache.set('pk_card', pk_card, settings.REDIS_TIMEOUT)
            cache.set('pk_cur', pk_cur, settings.REDIS_TIMEOUT)
            cache.set('pk_hold', 0, settings.REDIS_TIMEOUT)
            cache.set('pk_start', 1, settings.REDIS_TIMEOUT)
        # print(cache.get('pk_card'))

        if (pk_num == 3):
            pk_user = ["东", "北", "西", "无"]

            p0 = pk_all[:18]
            p0.sort()
            p1 = pk_all[18:36]
            p1.sort()
            p2 = pk_all[36:54]
            p1.sort()
            p3 = []
            pk_card = [p0,p1,p2,p3]
            pk_cur = []
            pk_dict = {
                'players': pk_user,
                'userid': userid,
                'holdid': 0,
                'msg': pk_msg,
                }
            cache.set('pk_card', pk_card, settings.REDIS_TIMEOUT)
            cache.set('pk_cur', pk_cur, settings.REDIS_TIMEOUT)
            cache.set('pk_hold', 0, settings.REDIS_TIMEOUT)
            cache.set('pk_start', 1, settings.REDIS_TIMEOUT)
        # print(cache.get('pk_card'))


        if (pk_num == 2):
            pk_user = ["东", "北", "无", "无"]

            p0 = pk_all[:20]
            p0.sort()
            p1 = pk_all[20:40]
            p1.sort()
            p2 = []
            p3 = []
            pk_card = [p0,p1,p2,p3]
            pk_cur = []
            pk_dict = {
                'players': pk_user,
                'userid': userid,
                'holdid': 0,
                'msg': pk_msg,
                }
            cache.set('pk_card', pk_card, settings.REDIS_TIMEOUT)
            cache.set('pk_cur', pk_cur, settings.REDIS_TIMEOUT)
            cache.set('pk_hold', 0, settings.REDIS_TIMEOUT)
            cache.set('pk_start', 1, settings.REDIS_TIMEOUT)
        # print(cache.get('pk_card'))


    return JsonResponse(pk_dict, safe=False)  