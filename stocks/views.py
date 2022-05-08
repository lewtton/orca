from django.shortcuts import render, HttpResponse
from datetime import datetime
import requests
from .models import StockList


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = '<br>'.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
# Create your views here.
def getStockInfo(name):

    data=[]
    url = "http://hq.sinajs.cn/list="+name
    # print(url)
    # url = "baidu.com"
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url,headers=kv)
    # print(r.apparent_encoding)
    mystr=r.text
    print(mystr)
    if len(mystr)>50:
        data=r.text[21:-3].split(",")
        print(data)
    else:
        data=[]
    return info




def rnfo(request):
    time = datetime.now()
    return HttpResponse("Hello World! 1111I came then left <br>"
    + time.strftime("%Y-%m-%d  %H:%M:%S"))

def showlist(request):
    return render(request, "list.html")

def info(request):
    if request.method == "POST":
        sname = request.POST.get("sname", None)
        infos=getStockInfo(sname)
        if len(infos) == 0:
            return HttpResponse("贱婢，你输入的股票代码有问题！！！")
        else:
            return render(request, "info.html", {
                'data': infos
        })

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)