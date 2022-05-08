from django.shortcuts import render, HttpResponse
from django.http import JsonResponse



def index(request):
    output="help me"
    return HttpResponse(output)
# Create your views here.

def table(request, userid):
    # return HttpResponse(userid)
    return render(request, "poker/index.html")

def yard(request):
    output="选择位置"
    return HttpResponse(output)

    # return render(request, "poker/index.html")
