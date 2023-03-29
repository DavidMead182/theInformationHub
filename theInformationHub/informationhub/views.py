from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    context_dic = {}
    context_dic['homepage'] = "active"

    return render(request,'homepage.html', context=context_dic)

def portfolio(request):
    context_dic = {}
    context_dic['portfolio'] = "active"
    return render(request,'portfolio.html', context=context_dic)

def about(request):
    context_dic = {}
    context_dic['about'] = "active"
    return render(request,'about.html', context=context_dic)

def myChatGla(request):
    context_dic = {}
    context_dic['portfolio'] = "active"
    return render(request,'myChatGla.html', context=context_dic)

def heartbeat(request):
    context_dic = {}
    context_dic['portfolio'] = "active"
    return render(request,'heartbeat.html', context=context_dic)

def thinformationhubsite(request):
    context_dic = {}
    context_dic['portfolio'] = "active"
    return render(request,'thinformationhubsite.html', context=context_dic)
