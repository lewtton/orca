import socket as ss
import random

from django.shortcuts import render
from django.http import JsonResponse
from stocks.models import StockList


MENULIST = [
    ['智能家居', '语言识别', '嵌入式开发', '树莓派', '低功耗蓝牙', '软件无线电'],
    ['图像分析', '视频流处理', '无头浏览器', '分析报告'],
    ['股票查询', '定时爬虫计划', '图表'],
]
def poker(request):

    return render(request, "poker/index.html")

def pokerapi(request):
    """
    HOP
    """
    
    pk_user = ["郭靖", "黄蓉", "令狐冲", "任盈盈"]
    pk_card = [[1,3,5,7,9,11,22,33,44,50],[2,4,6,8,22],[21,23,25],[31,35,37],[31,35,37]]
    pk_cur  = 2
    pk_dict = [pk_user,pk_card,pk_cur]


    # print("字典：" + str(sta_dict))
    return JsonResponse(pk_dict, safe=False)  

def renderhome(request, menu_id):
    """
    HOP
    """
    # stock_list = StockList.objects.order_by('-starttime')[:50]
    # print(stock_list)
    mdiv = {
        'MENULIST':MENULIST,
        'menu_id':menu_id,
        'page_name':MENULIST[menu_id//10-1][menu_id%10-1],
        'context':'Blablabla...!!!',
        # 'stock_list':stock_list
        }
    # mdiv['MENULIST']=genPageMenuHtmlCode(11)
    response = render(request, "index.html", mdiv)
    print(type(response))
    return response


def home(request):
    """
    HOP
    """
    response = renderhome(request, 11)
    return response

def menu(request, menu_id):
    """
    HOP
    """
    response = renderhome(request, menu_id)
    return response

def smarthomeapi(request):
    """
    HOP
    """
    host = '10.10.10.44'
    port = 8090
    btn_str = str(request.POST.get("btn")).upper()
    print(btn_str)
    so_tcp = ss.socket(ss.AF_INET, ss.SOCK_STREAM)
    sta = ""
    sta_dict = {'item':'none'}
    so_tcp.connect((host, port))
    so_tcp.send(btn_str.encode('utf-8'))
    sta = so_tcp.recv(1024).decode('utf-8')
    so_tcp.close()
    # print("列表："+sta)
    sta_list = []
    sta_dict = {}
    sta_list = sta.split(",")
    for i,item in enumerate(sta_list):
        sta_dict[i+1] = item
    # print("字典：" + str(sta_dict))
    return JsonResponse(sta_dict, safe=False)
    
