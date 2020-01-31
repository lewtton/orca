import random, redis, os, locale
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core.cache import cache
from django.conf import settings




def apipk(request):
    """
    HOP
    """
    print(request.POST)
    # print("init:",type(request.POST.get("init")))
    # print("suit:",type(request.POST.get("suit")))
    # print("card:",type(request.POST.get("card")))
    # print("sync:",type(request.POST.get("sync")))

    pk_dict = {}
    if(request.POST.get("suit")=="1"):
        suitcard = request.POST.get("card").split(",")
        suitnum = request.POST.get("num").split(",")
        suitnum.reverse()
        # print(suitnum)        
        # print(suitnum)
        for i in suitnum:
            pk_card[0].pop(int(i))
            
        pk_card = cache.get('pk_card')
        pk_cur = cache.get('pk_cur')
        pk_cur.append(suitcard)
        cache.set('pk_cur', pk_cur, settings.REDIS_TIMEOUT)
        cache.set('pk_card', pk_card, settings.REDIS_TIMEOUT)

        print(pk_cur)
        print(pk_card)
        # print(cache.get('p0'))
        pk_dict = {
            'cards': pk_card,
            'cur': suitcard,
            }
        
    if(request.POST.get("suit")=="2"):
        pk_cur = cache.get('pk_cur')
        pk_card = cache.get('pk_card')
        suitcard=pk_card.pop()
        print(len(suitcard))
        print(suitcard)
        if (suitcard):    
            pk_card[0].append(suitcard)
            print(suitcard)
            print(pk_cur)
            print(pk_card)
            cache.set('pk_card', pk_card, settings.REDIS_TIMEOUT)
            cache.set('pk_cur', pk_cur, settings.REDIS_TIMEOUT)
        pk_dict = {
            'cards': pk_card,
            'cur': suitcard,
            }      

    if(request.POST.get("init")=="1"):
        pk_all = list(range(54))
        # print(pk_all)
        random.shuffle(pk_all)
        # print(pk_all)
        p0 = pk_all[:14]
        p0.sort()
        p1 = pk_all[14:28]
        p1.sort()
        p2 = pk_all[28:41]
        p2.sort()
        p3 = pk_all[41:54]
        p3.sort()

        pk_user = ["郭靖", "黄蓉", "令狐冲", "任盈盈", 2]
        pk_card = [p0,p1,p2,p3]
        pk_cur = []
        pk_dict = {
            'users': pk_user,
            'cards': pk_card,
            'cur': pk_cur,
            }
        cache.set('pk_card', pk_card, settings.REDIS_TIMEOUT)
        cache.set('pk_cur', pk_cur, settings.REDIS_TIMEOUT)
        # print(cache.get('pk_card'))

    # pk_all = list(range(54))
    # # print(pk_all)
    # random.shuffle(pk_all)
    # # print(pk_all)
    # p0 = pk_all[:14]
    # p0.sort()
    # p1 = pk_all[14:28]
    # p1.sort()
    # p2 = pk_all[28:41]
    # p2.sort()
    # p3 = pk_all[41:54]
    # p3.sort()

    # pk_user = ["郭靖", "黄蓉", "令狐冲", "任盈盈", 2]
    # pk_card = {'p0':p0,'p1':p1,'p2':p2,'p3':p3,'p_cur':[31,35,37]}
    # pk_dict = {
    #     'users': pk_user,
    #     'cards': pk_card,
    #     }
    # print("Responsed: "+str(pk_dict))

    return JsonResponse(pk_dict, safe=False)  