from django.shortcuts import render, HttpResponse
from datetime import datetime
import requests



def index(request):
    output="help me"
    return HttpResponse(output)
# Create your views here.

def poker(request):

    return render(request, "poker/index.html")



def getStockInfo(name):
    try:
        info=[]
        url = "http://hq.sinajs.cn/list="+name
        # print(url)
        # url = "baidu.com"
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url,headers=kv)
        # print(r.apparent_encoding)
        mystr=r.text
        print(mystr)
        if len(mystr)>50:
            info=r.text[21:-3].split(",")
            print(info)
        else:
            info=[]
        return info
            
    except:
        pass



def rnfo(request):
    time = datetime.now()
    return HttpResponse("Hello World! 1111I came then left <br>"
    + time.strftime("%Y-%m-%d  %H:%M:%S"))

def showlist(request):
    return render(request, "list.html")

def info(request):
    if request.method == "POST":
        sname = request.POST.get("sname", None)
        info=getStockInfo(sname)
        if info==[]:
            return HttpResponse("贱婢，你输入的股票代码有问题！！！")
        else:
            return render(request, "info.html", {
                'data': info
        })

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)