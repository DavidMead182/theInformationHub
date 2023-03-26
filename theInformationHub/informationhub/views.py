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